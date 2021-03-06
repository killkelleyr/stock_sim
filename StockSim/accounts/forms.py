from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
        error_messages = {
            'email': {
                'unique': 'My Custom Error Message here !!!',
            },
        }

class SetupAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['rhoodID', 'rhoodPWD', 'rhQ']