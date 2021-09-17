from django.conf.urls import include, url
from django.urls.conf import path

from . import views # import views so we can use them in urls.

urlpatterns = [
    path('dataproducts', views.PublisherListView.get_products_by_cat, name='products_cat'),
    path('publisher/data', views.PublisherListView.get_favorite_products, name='fav_products'),
    path('detailproduct/<int:pk>', views.PublisherListView.detail_prod, name='product_detail'),
]