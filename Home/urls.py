from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('contact',views.contact),
    path('about',views.about),
    # path('qr',views.qr),
    path('qr',views.upload_csv),
    path('cookiesexample',views.cookiesexample),
]