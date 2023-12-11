
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']