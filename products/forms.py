from django import forms

class ProductForm(forms.Form):
    product_form = forms.CharField(label='Product form', max_length=100)

class IdForm(forms.Form):
    id_product = forms.CharField(label='id product', max_length=50)