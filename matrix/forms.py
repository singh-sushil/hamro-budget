from django import forms
from .models import signup
from django.forms import ModelForm
class sign_up(ModelForm):
    class Meta:
        model = signup
        fields = ['name', 'citizenship_no','photo','citizenship_scan','username','password1','password2']  
        widgets={ 
            'name':forms.TextInput(attrs = {
                'placeholder':'enter your firstname'
            }),
            'citizenship_no':forms.TextInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'photo':forms.ClearableFileInput(attrs = {
                'placeholder':'enter your username'
                }),
            'citizenship_scan':forms.ClearableFileInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'username':forms.PasswordInput(attrs = {'placeholder':'type ur password'}),
            'password1':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
            'password2':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
        }

