from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    nationalcode = forms.CharField(required=True, label="National Code")
    FullName = forms.CharField(required=True, label="Full Name")
    Adress = forms.CharField(required=True, label="Adress")
    class Meta:
        model = User
        fields = ('FullName','username', 'email','nationalcode','Adress','password1', 'password2')