from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('registration', views.Registration),
    path('login', views.user_login),
    path('logout',views.userlogout)
   
    
]
