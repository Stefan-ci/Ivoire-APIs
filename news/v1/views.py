import random, json, hashlib
from django.db.models import Q
from news.models import Article
from core.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from news.v1.serializers import ArticleSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_423_LOCKED
from rest_framework.status import HTTP_200_OK, HTTP_511_NETWORK_AUTHENTICATION_REQUIRED




@api_view(['GET'])
def articles_list_view(request):
    articles = Article.objects.filter(is_public=True)

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass

    if 'category' in request.GET:
        category = request.GET['category']
        articles = articles.filter(category=category)


    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )
    
    
    if 'pageSize' in request.GET:
        try:
            if int(request.GET['pageSize']) >= 20:
                paginator = Paginator(articles, 20)
            paginator = Paginator(articles, int(request.GET['pageSize']))
        except:
            paginator = Paginator(articles, 20)

    else:
        paginator = Paginator(articles, 20)
    

    page = request.GET.get("page")
    articles_obj = paginator.get_page(page)
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    data = {
        'total_articles': articles_obj.__len__(),
        'articles': ArticleSerializer(articles_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')














@api_view(['GET'])
def random_articles_list_view(request):
    articles = Article.objects.filter(is_public=True)

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass

    if 'category' in request.GET:
        category = request.GET['category']
        articles = articles.filter(category=category)

    if len(articles) >= 20:
        articles = random.sample(list(articles), 20)
    

    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )

    if 'pageSize' in request.GET:
        try:
            if int(request.GET['pageSize']) >= 20:
                paginator = Paginator(articles, 20)
            paginator = Paginator(articles, int(request.GET['pageSize']))
        except:
            paginator = Paginator(articles, 20)
    else:
        paginator = Paginator(articles, 20)
    
    page = request.GET.get("page")
    articles_obj = paginator.get_page(page)
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    data = {
        'articles_total': articles_obj.__len__(),
        'articles': ArticleSerializer(articles_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')












@api_view(['GET'])
def random_article_view(request):
    articles = Article.objects.filter(is_public=True, is_premium=False)

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass
    

    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )


    random_article = random.sample(list(articles), 1)

    data = ArticleSerializer(random_article, many=True).data
    return Response(data, status=HTTP_200_OK, content_type='application/json')











@api_view(['GET'])
def article_detail_view(request, pk):
    
    articles = Article.objects.filter(is_public=True, is_premium=False)
    
    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                print(f'Profile matched: {profile.user.username}')
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass
    
    

    article = get_object_or_404(articles, pk=pk)


    data = ArticleSerializer(article, many=False).data
    return Response(data, status=HTTP_200_OK, content_type='application/json')












@api_view(['GET', 'POST'])
def article_detail_with_related_view(request, pk):
    articles = Article.objects.filter(is_public=True, is_premium=False)

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass
        
    
    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )
    

    article = get_object_or_404(articles, pk=pk)

    category = article.category
    similar_articles = articles.filter(category=category).exclude(pk=article.pk)
    if len(similar_articles) >= 6:
        similar_articles = random.sample(list(similar_articles), 6)
    
    data = {
        'article': ArticleSerializer(article, many=False).data,
        'similar_articles_count': similar_articles.__len__(),
        'similar_articles': ArticleSerializer(similar_articles, many=True).data,
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')
















@api_view(['GET'])
def articles_by_category_list_view(request, category:str):
    articles = Article.objects.filter(is_public=True, is_premium=False, category=category)
    
    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass

    if len(articles) >= 20:
        articles = random.sample(list(articles), 20)
    
    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )

    if 'pageSize' in request.GET:
        try:
            paginator = Paginator(articles, int(request.GET['pageSize']))
        except:
            paginator = Paginator(articles, 20)
    else:
        paginator = Paginator(articles, 20)
    
    page = request.GET.get("page")
    articles_obj = paginator.get_page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    data = {
        'articles_total': articles_obj.__len__(),
        'articles': ArticleSerializer(articles_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')










@api_view(['GET', 'POST'])
def submit_article_view(request):
    if request.method == 'POST':
        if 'apiKey' in request.headers:
            try:
                hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
                hashed_key = hashlib.sha256(hash_str).hexdigest()
                profile = Profile.objects.get(hashed_api_key=hashed_key)
                if profile:
                    serializer = ArticleSerializer(data=request.data)
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








@api_view(['GET'])
def search_articles_view(request):
    articles = Article.objects.filter(is_public=True, is_premium=False)

    if 'apiKey' in request.headers:
        try:
            hash_str = json.dumps(request.headers['apiKey'], sort_keys=True).encode()
            hashed_key = hashlib.sha256(hash_str).hexdigest()
            profile = Profile.objects.get(hashed_api_key=hashed_key)
            if profile:
                articles = Article.objects.filter(is_public=True, is_premium=True)
        except:
            pass

    if 'category' in request.GET:
        category = request.GET['category']
        articles = articles.filter(category=category)


    if 'q' in request.GET:
        query = request.GET['q']

        if query is not None:
            articles = articles.filter(
                Q(title__contains=query)|
                Q(author__contains=query)|
                Q(content__contains=query)|
                Q(summary__contains=query)|
                Q(tags__contains=query)|
                Q(category__contains=query)|
                Q(language__contains=query)|
                Q(website__contains=query)
            )
    
    
    if 'pageSize' in request.GET:
        try:
            if int(request.GET['pageSize']) >= 20:
                paginator = Paginator(articles, 20)
            paginator = Paginator(articles, int(request.GET['pageSize']))
        except:
            paginator = Paginator(articles, 20)
    else:
        paginator = Paginator(articles, 20)
    

    page = request.GET.get("page")
    articles_obj = paginator.get_page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    data = {
        'results': ArticleSerializer(articles_obj, many=True).data
    }

    return Response(data, status=HTTP_200_OK, content_type='application/json')









