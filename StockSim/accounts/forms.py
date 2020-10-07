from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        error_messages = {
            'email': {
                'unique': 'My Custom Error Message here !!!',
            },
        }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('alertinnovation.com'):
            raise forms.ValidationError("not a valid Alert Innovation email", code='invalid email')
        return email