from django.shortcuts import render
from thinkahead.forms import LoginForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    context = {}
    form = LoginForm(request.POST)
    context['form']=form

    #Ensure login fields are filled out
    if form.is_valid():
        current_user = authenticate(username=context['username'],password=request.POST['password'])
        #If user info is correct, retrieve login count
        if current_user:
            login(request,current_user)
        else:
            return render(request, 'home.html',RequestContext(request,{'errors':"Invalid Username/Password. Please try again."}))
    else:
        return render(request, 'home.html',RequestContext(request,{'errors':form.errors}))

def user_creation(request):
    context = {}
    form = LoginForm(request.POST)
    context['form']=form
    username, password = request.POST['username'],request.POST['password']
    
    #Check user/password and ensure meets requirements
    if form.is_valid():
        return render(request, 'home.html',RequestContext(request,{'errors':"Username/Password cannot be left blank."}))
        
    #Checks whether user already exists    
    if User.objects.filter(username=request.POST['username']):
        return render(request, 'register.html',RequestContext(request,{'errors':"Username is already taken."}))
        
    new_user = User.objects.create_user(username=username,password=password)
    new_user.save()
    new_user = authenticate(username=context['username'],password=request.POST['password']) #django requires authentification before logging in
    login(request,new_user)
    return render(request, 'register.html', RequestContext(request,{}))


def user_registration(request):
    if not request.user.isauthenticated():
        return render(request, 'home.html',RequestContext(request,{'errors':"Username/Password cannot be left blank."}))

def user_logout(request):
    if request.user.isauthenticated() and 'logout' in request.POST:
        #User was logged in and the logout button was pressed
        logout(request)
    return render(request, 'home.html', RequestContext(request,{}))
        