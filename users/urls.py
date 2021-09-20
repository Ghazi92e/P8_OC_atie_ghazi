from . import views
from django.conf.urls import include
from django.urls.conf import path


urlpatterns = [
    path('register', views.user_register, name='register'),
    path('login/', views.login_user),
    path('connected', views.index),
    path('login/deconnexion/', views.logout_user),
    path('account', views.user_account),
]