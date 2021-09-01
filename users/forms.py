from django import forms

class RegisterUsers(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password', max_length=128, widget=forms.PasswordInput)
