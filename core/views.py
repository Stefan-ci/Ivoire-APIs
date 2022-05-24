from django.contrib import messages
from django.http import HttpResponse
from core.forms import CreateUserForm
from core.models import Documentation
from django.shortcuts import redirect, render
from core.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout





def home_view(request):
    
    context = {}

    template_name = 'public/home.html'
    return render(request, template_name, context)









def apis_documentations_view(request):
    docs = Documentation.objects.filter(is_public=True)

    context = {'docs': docs}

    template_name = 'public/api/documentations.html'
    return render(request, template_name, context)













def api_documentation_view(request, version:str):
    context = {}
    docs = Documentation.objects.filter(is_public=True, version=version)
    doc = docs.last()
    
    if doc:
        context.update({'api_doc': doc})
    
    if not doc:
        messages.error(request, f"There is no API associated with specified version ({version})")
        print(f"There is no API associated with specified version ({version})")
        return redirect('home')

    template_name = 'public/api/api_documentation.html'
    return render(request, template_name, context)














@unauthenticated_user
def register_view(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST) or None
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.age = age
            profile.sex = sex
            profile.save()
            
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, "Your account has been created successfully !")
                return redirect('profile')
            else:
                messages.warning(request, "Your account is not active yet. Please contact the support")
                return redirect('home')
        else:
            messages.error(request, "Form is not valid, please check again retry !!!")
            return redirect('register')
    
    else:
        form = CreateUserForm()
    
    context = {}

    template_name = 'public/accounts/register.html'
    return render(request, template_name, context)











@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out, Good bye !")
    return redirect('login')









@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, "You're logged in successfully now !")
            return redirect('profile')
        else:
            messages.error(request, "Connection aborted, refresh and try again please!")
            return redirect('login')
        
    context = {}

    template_name = 'public/accounts/login.html'
    return render(request, template_name, context)










@login_required(login_url='login')
def user_profile_view(request):
    context = {}
    template_name = 'public/accounts/profile.html'
    return render(request, template_name, context)





















