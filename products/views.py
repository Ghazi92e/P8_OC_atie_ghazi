from django.db import reset_queries
from products.models import Categories, Product, Product_favorite
from django.views.generic import ListView
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import IdForm, NameForm

class PublisherListView(ListView):
      
    @login_required(login_url='/users/login/')
    def get_favorite_products(request):
        form = NameForm(request.GET)
        data_fav = None
        current_user = request.user
        data_fav = Product_favorite.objects.filter(user_id=current_user.id)
        if 'datatest' in request.POST:
            user_id = User.objects.get(pk=current_user.id)
            product_id = Product.objects.get(pk=request.POST['datatest'])
            Product_favorite.add_favorite_products(user_id, product_id)
        return render(request, 'products/product_favorite.html', {'data_fav': data_fav, 'form': form })
        
    def get_products_by_cat(request):
        query = None
        if request.method == 'GET':
            form = NameForm(request.GET)
            if form.is_valid():
                data = form.cleaned_data['your_name']
                pub = get_object_or_404(Categories, name=data)
                query = Product.objects.filter(categories=pub).order_by('nutriscore')
                return render(request, 'products/products_by_categories.html', {'form': form, 'q': query})
            else:
                form = NameForm()
        return render(request, 'purbeurre_project/home.html', {'form': form, 'q': query})

    def detail_prod(request, pk):
        form = NameForm(request.GET)
        product = Product.objects.get(pk=pk)
        return render(request, 'products/product_detail.html', context={'product': product, 'form': form })