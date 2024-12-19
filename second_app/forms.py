from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class Registratin_form(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class ComentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields=['name','email','body']

class change_data(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ['username','email','first_name','last_name']