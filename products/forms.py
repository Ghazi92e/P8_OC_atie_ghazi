from django import forms


class ProductForm(forms.Form):
    # form for search categories products
    product_form = forms.CharField(label='Product form', max_length=100)


class IdForm(forms.Form):
    # form to get id products
    id_product = forms.CharField(label='id product', max_length=50)
