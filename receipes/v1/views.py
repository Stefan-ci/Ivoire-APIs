import random, json, hashlib
from receipes.models import Receipe
from core.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from receipes.v1.serializers import ReceipeSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_423_LOCKED
from rest_framework.status import HTTP_200_OK, HTTP_511_NETWORK_AUTHENTICATION_REQUIRED







@api_view(['GET'])
def receipes_list_view(request):
    receipes = Receipe.objects.filter(is_public=True).using('receipes')

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass

    if 'category' in request.GET:
        category = request.GET['category']
        receipes = receipes.filter(category=category)

    
    
    if 'count' in request.GET:
        try:
            if int(request.GET['count']) >= 20:
                paginator = Paginator(receipes, 20)
            paginator = Paginator(receipes, int(request.GET['count']))
        except:
            paginator = Paginator(receipes, 20)

    else:
        paginator = Paginator(receipes, 20)
    

    page = request.GET.get("page")
    receipes_obj = paginator.get_page(page)
    
    try:
        receipes = paginator.page(page)
    except PageNotAnInteger:
        receipes = paginator.page(1)
    except EmptyPage:
        receipes = paginator.page(paginator.num_pages)

    data = {
        'total_receipes': receipes_obj.__len__(),
        'receipes': ReceipeSerializer(receipes_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')



















@api_view(['GET'])
def random_receipes_list_view(request):
    receipes = Receipe.objects.filter(is_public=True).using('receipes')

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass

    if 'category' in request.GET:
        category = request.GET['category']
        receipes = receipes.filter(category=category)

    if len(receipes) >= 20:
        receipes = random.sample(list(receipes), 20)

    if 'count' in request.GET:
        try:
            if int(request.GET['count']) >= 20:
                paginator = Paginator(receipes, 20)
            paginator = Paginator(receipes, int(request.GET['count']))
        except:
            paginator = Paginator(receipes, 20)
    else:
        paginator = Paginator(receipes, 20)
    
    page = request.GET.get("page")
    receipes_obj = paginator.get_page(page)
    
    try:
        receipes = paginator.page(page)
    except PageNotAnInteger:
        receipes = paginator.page(1)
    except EmptyPage:
        receipes = paginator.page(paginator.num_pages)
    
    data = {
        'receipes_total': receipes_obj.__len__(),
        'receipes': ReceipeSerializer(receipes_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')













@api_view(['GET'])
def random_receipe_view(request):
    receipes = Receipe.objects.filter(is_public=True, is_premium=False).using('receipes')

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass


    random_receipe = random.sample(list(receipes), 1)

    data = ReceipeSerializer(random_receipe, many=True).data
    return Response(data, status=HTTP_200_OK, content_type='application/json')















@api_view(['GET'])
def receipe_detail_view(request, pk):
    
    receipes = Receipe.objects.filter(is_public=True, is_premium=False).using('receipes')
    
    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                print(f'Profile matched: {profile.user.username}')
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass
    

    receipe = get_object_or_404(receipes, pk=pk)


    data = ReceipeSerializer(receipe, many=False).data
    return Response(data, status=HTTP_200_OK, content_type='application/json')














@api_view(['GET', 'POST'])
def receipe_detail_with_related_view(request, pk):
    receipes = Receipe.objects.filter(is_public=True, is_premium=False).using('receipes')

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass
    

    receipe = get_object_or_404(receipes, pk=pk)

    category = receipe.category
    similar_receipes = receipes.filter(category=category).exclude(pk=receipe.pk)
    if len(similar_receipes) >= 6:
        similar_receipes = random.sample(list(similar_receipes), 6)
    
    data = {
        'receipe': ReceipeSerializer(receipe, many=False).data,
        'similar_receipes_count': similar_receipes.__len__(),
        'similar_receipes': ReceipeSerializer(similar_receipes, many=True).data,
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')


















@api_view(['GET'])
def receipes_by_category_list_view(request, category:str):
    receipes = Receipe.objects.filter(is_public=True, is_premium=False, category=category).using('receipes')
    
    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                receipes = Receipe.objects.filter(is_public=True, is_premium=True).using('receipes')
        except:
            pass

    if len(receipes) >= 20:
        receipes = random.sample(list(receipes), 20)

    if 'count' in request.GET:
        try:
            paginator = Paginator(receipes, int(request.GET['count']))
        except:
            paginator = Paginator(receipes, 20)
    else:
        paginator = Paginator(receipes, 20)
    
    page = request.GET.get("page")
    receipes_obj = paginator.get_page(page)

    try:
        receipes = paginator.page(page)
    except PageNotAnInteger:
        receipes = paginator.page(1)
    except EmptyPage:
        receipes = paginator.page(paginator.num_pages)
    
    data = {
        'receipes_total': receipes_obj.__len__(),
        'receipes': ReceipeSerializer(receipes_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')












@api_view(['GET', 'POST'])
def submit_receipe_view(request):
    if request.method == 'POST':
        if 'apiKey' in request.headers:
            try:
                hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
                hashed_key = hashlib.sha256(hash_str).hexdigest()
                profile = Profile.objects.get(hashed_api_key=hashed_key)
                if profile:
                    serializer = ReceipeSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save(submited_by=profile.user, is_submited=True)
                        return Response(serializer.data, status=HTTP_200_OK)
                    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            except:
                msg = {"detail": "Sorry, Your API key is invalid"}
                return Response(msg, status=HTTP_423_LOCKED)
        
        else:
            err = """
                Sorry, You must include your API key in headers. 
                If you haven't any API key, feel free to sign up and get one !!"
            """
            msg = {"detail": err}
            return Response(msg, status=HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
    else:
        msg = {"detail": "Sorry, You may send a valid POST request along with your API key !!"}
        return Response(msg, status=HTTP_405_METHOD_NOT_ALLOWED)





