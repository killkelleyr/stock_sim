from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views import generic

from django.shortcuts import render, redirect
from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm
from .models import Account
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

import pyEX as p
import os

#@unauthenticated_user
def loginUser(request):
    #form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:home')
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

@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
    template_name='accounts/index.html'

    def get(self, request):
        context={}
        accountDetails = Account.objects.get(user=request.user)
        if not accountDetails.rhoodID or not accountDetails.rhoodPWD or not accountDetails.rhQ:
            context['newUser'] = True
        #TODO: now that we know if its a new user, we must get the user to provide their RH credentials if they are new
        #This should be displayed as a modal
        
        
        
        token=os.environ['API_TOKEN']
        platform=os.environ['API_PLATFORM']
        c=p.Client(api_token=token, version=platform)
        dow=c.quote('DOW')
        sp500=c.quote('SPY')
        nasdaq=c.quote('IWM')
        context['current']={
            'dow':{'price':dow['latestPrice'], 'change':dow['changePercent']}, 
            'sp500':{'price':sp500['latestPrice'], 'change':sp500['changePercent']}, 
            'nasdaq':{'price':nasdaq['latestPrice'], 'change':nasdaq['changePercent']}
            }
        #return HttpResponse(context)
        return render(request, self.template_name, context)