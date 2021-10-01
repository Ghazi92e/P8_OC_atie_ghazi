from django import forms


class RegisterUsers(forms.Form):
    '''
    Create a form for user registration
    '''
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password',
                               max_length=128, widget=forms.PasswordInput)
    email = forms.EmailField(label='email', max_length=256)
