from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('getAllState', views.getAllState),
    path('insertState', views.insertState),
    path('insertStateUsingJson', views.insertStateUsingJson),
    path('deleteState', views.deleteState),
    path('deleteStatePara/<int:id>', views.deleteStatePara),
    path('updateStatePara/<int:id>', views.updateStatePara),
    path('clogin', views.clogin),
    path('checkregistration', views.checkregistration),
]
