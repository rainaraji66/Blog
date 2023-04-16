from dataclasses import fields
from random import choices
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile





class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    CHOICES=[('Male','Male'),
         ('Female','Female'),
         ('Trans','Trans')]

    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1980,2022)))


    class Meta:
            model = User
            fields = ['username','email','gender','date_of_birth','password1','password2']

class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()


     class Meta:
            model = User
            fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
     

     class Meta:
            model = Profile
            fields = ['image']
