from django.conf.urls import include, url
from django.urls.conf import path

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('publisher/', views.PublisherListView.get_name),
    path('publisher/data', views.PublisherListView.get_products),
    path('publis/', views.PublisherListView.as_view()),
    path('<publisher>/', views.PublisherListView.as_view()),
  # "/store" will call the method "index" in "views.py"
]