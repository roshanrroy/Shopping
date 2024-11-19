from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('cart',views.cart),
    path('delete_cart_item/<int:cart_id>',views.delete_cart_item),
    path('loadcart',views.loadcart),
]