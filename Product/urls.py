from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('product', views.product),
    path('detail/<int:id>', views.detail),
    path('add_to_cart',views.add_to_cart)
    
]