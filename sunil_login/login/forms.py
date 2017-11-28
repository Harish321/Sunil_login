from django import forms
from django.forms import CharField,TextInput,IntegerField,
from .models import user,sunil,check_login

class Login_Form(forms.Form):
    username = CharField(widget=TextInput(attrs={'id':'username'}))
    password = forms.CharField(widget=forms.PasswordInput)