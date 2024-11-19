from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('Admincategory', views.viewdata),
    path('adddata',views.adddata),
    path('deletedata/<int:id>',views.deletedata),
    path('editdata/<int:id>',views.editdata)
]

