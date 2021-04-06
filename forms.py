from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Items


class sign_upForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    error_messages = {
        'username': {
            'unique': 'Your Custom Error Message here !!!',
        },
    }

class UploadForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('id','names', 'surname','cell_number','email','street','city','province','country_code','item_type','item_name', 'item_pic')

