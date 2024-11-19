from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('order', views.order),
    path('item/<int:order_id>', views.item),
    
    
]