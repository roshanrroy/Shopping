from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('state',views.state),
    path('city',views.city),
    path('citybystate',views.citybystate)
]