
from django.shortcuts import render
from products.forms import ProductForm


class Home():
    def mentionslegales(request):
        form = ProductForm(request.GET)
        return render(request, 'mentionslegales.html', {'form': form})
