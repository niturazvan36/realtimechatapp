from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
                    'username': forms.TextInput(attrs={'placeholder': 'Username'}),
                    'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
                 'password1': forms.TextInput(attrs={'placeholder': 'Enter Password'}),
                 'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
                }