from django import forms
from .models import signup,local_bodies_id,comment
from django.forms import ModelForm
class sign_up(ModelForm):
    class Meta:
        model = signup
        fields = ['name', 'citizenship_no','photo','citizenship_scan','username','password','confirm_password']  
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
            'username':forms.TextInput(attrs = {'placeholder':'type ur username'}),
            'password':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
            'confirm_password':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
        }

class official_login(ModelForm):
    class Meta:
        model = local_bodies_id
        fields = ['username','password']  
        widgets={ 
            'username':forms.TextInput(attrs = {
                'placeholder':'enter your firstname'
            }),
            'password':forms.PasswordInput(attrs = {'placeholder':'enter your password'}),
        }
class user_login(ModelForm):
    class Meta:
        model = signup
        fields = ['username','password']  
        widgets={ 
            'username':forms.TextInput(attrs = {
                'placeholder':'enter your firstname'
            }),
            'password':forms.PasswordInput(attrs = {'placeholder':'enter your password'}),
        }

class user_comment(ModelForm):
    class Meta:
        model = comment
        fields = ['feedback']
        widgets = {
            'feedback':forms.Textarea(attrs = {
                'placeholder':'give your feedback',
                'rows':4,
                'cols':30
            }),
        }