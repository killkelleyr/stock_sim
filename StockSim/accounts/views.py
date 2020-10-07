from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.shortcuts import render, redirect
from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm

#@unauthenticated_user
def loginUser(request):
    #form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio:home')
        else:
            messages.info(request, 'Incorrect Username/Password')
    context = {} 
    return render(request, 'accounts/login.html', context=context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created for user: {}'.format(form.cleaned_data.get('username')))
            return redirect('accounts:loginUser')
    
    context = {'form':form} 
    return render(request, 'accounts/register.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('accounts:loginUser' )

@login_required(login_url='accounts:loginUser')
#@allowed_users(allowed_roles=[])
def userProfile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)