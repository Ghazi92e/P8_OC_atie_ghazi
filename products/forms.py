from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class IdForm(forms.Form):
    id_product = forms.CharField(label='id product', max_length=50)