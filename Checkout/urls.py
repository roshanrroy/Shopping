from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('checkout',views.checkout),
    path('create_order',views.create_order),
    path('order_entry',views.order_entry)
    # path('statebycountry',views.statebycountry)
]