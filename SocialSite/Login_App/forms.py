from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 
from Login_App.models import UserProfile


# forms 

class CreateNewUserForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={
        'placeholder':'Enter Email Address'}) ,required=True)
    username =forms.CharField(label='',widget=forms.TextInput(attrs={
        'placeholder':'username'}),required=True)
    password1 = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={
        'placeholder':'password'}))
    password2 = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={
        'placeholder':'password confirmation'}))

    class Meta():
        model = User
        fields = ('username','email','password1','password2',)
        

class LoginForm(AuthenticationForm):
    username =forms.CharField(label='',widget=forms.TextInput(attrs={
    'placeholder':'username'}),required=True)
    password = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={
    'placeholder':'password'}))
    
    class Meta():
        model = User
        fields = ('username','password')

        
class EditProfile(forms.ModelForm):
    dob = forms.DateField(label='Birth of Date',required=False,widget=forms.TextInput(attrs={
        'type':'date'
    }))
    class Meta():
        model = UserProfile
        exclude = ('xxx',)   