
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='',

        widget=forms.TextInput(attrs={
            'id': 'username',

        }))
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'id': 'password',

        }))

    email = forms.CharField(

        label='',
        widget=forms.EmailInput(attrs={
            'id': 'email',

        }))

    # remember_me = forms.BoolenField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # check if user already exist, raise the exception

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                u'Username "%s" is already in use.' % username)
        return username
    
     # check if email already exist, raise the exception

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                u'Email "%s" is already in use.' % email)
        return email

     # check if password is shorter than 5 character, raise the exception
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise forms.ValidationError("Password is too short")
        return password
