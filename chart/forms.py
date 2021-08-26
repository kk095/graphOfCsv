from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.forms import fields, widgets
from .models import Csvfile, Check



class Mysignup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class File(ModelForm):
    class Meta:
        modal=Check
        fields=['file',]

class Name(forms.Form):
    name=forms.CharField()


