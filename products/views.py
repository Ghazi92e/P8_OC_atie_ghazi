from products.models import Categories, Product, Product_favorite
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.forms import ProductForm


class PublisherListView(ListView):

    @login_required(login_url='/users/login/')
    def get_favorite_products(request):
        '''
        get favorite products from database saved by users
        '''
        form = ProductForm(request.GET)
        data_fav = None
        current_user = request.user
        data_fav = Product_favorite.objects.filter(user_id=current_user.id)
        if 'datatest' in request.POST:
            user_id = User.objects.get(pk=current_user.id)
            product_id = Product.objects.get(pk=request.POST['datatest'])
            Product_favorite.add_favorite_products(user_id, product_id)
        return render(request, 'products/product_favorite.html',
                      {'data_fav': data_fav, 'form': form})

    def get_products_by_cat(request):
        '''
        get products by categories send by users in search bar
        '''
        query = None
        form = None
        if request.method == 'GET':
            form = ProductForm(request.GET)
            if form.is_valid():
                data = form.cleaned_data['product_form']
                pub = get_object_or_404(Categories, name=data)
                query = Product.objects.filter(
                    categories=pub).order_by('nutriscore')
                return render(request, 'products/products_by_categories.html',
                              {'form': form, 'q': query})
            else:
                form = ProductForm()
        return render(request, 'purbeurre_project/home.html',
                      {'form': form, 'q': query})

    def detail_prod(request, pk):
        '''
        displays products details
        '''
        form = ProductForm(request.GET)
        product = Product.objects.get(pk=pk)
        return render(request, 'products/product_detail.html',
                      context={'product': product, 'form': form})
