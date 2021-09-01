from django.db import reset_queries
from products.models import Categories, Product
from django.views.generic import ListView
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .forms import IdForm, NameForm

class PublisherListView(ListView):
    """
     template_name = 'products/products_by_categories.html'
    def get_queryset(self):
        self.publisher = get_object_or_404(Categories, name=self.kwargs['publisher'])
        return Product.objects.filter(categories=self.publisher)
    """

    def get_products(request):
        #query = Product.objects.filter(categories__name='pizza')
        # if this is a POST request we need to process the form data

        #if 'prod' in request.POST:
        #    print("salut CA VA BIEN")
        print("testdeok")
        #if request.method == 'POST':
        if 'datatest' in request.POST:
            #d = request.POST
            print(request.POST['datatest'])

        return render(request, 'products/product_list.html')
        
    @login_required
    def get_name(request):
        #query = Product.objects.filter(categories__name='pizza')
        # if this is a POST request we need to process the form data
        print("okokokok")
        query = None
        if request.method == 'GET':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.GET)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                data = form.cleaned_data['your_name']
                pub = get_object_or_404(Categories, name=data)
                query = Product.objects.filter(categories=pub).order_by('nutriscore')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
        
        return render(request, 'products/products_by_categories.html', {'form': form, 'q': query})
    """
      def index(request):
        return render(request, 'products/base.html')
    """
    """
        def index(request):
                message = "Salut tout le monde !"
                context = {
                    'data': message,
                }
                return render(request, 'index.html', context=context)
    """