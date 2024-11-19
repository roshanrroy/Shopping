from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('AdminSubcategory', views.viewdata),
    path('adddata1',views.adddata),
    path('deletedata1/<int:id>',views.deletedata),
    path('editdata1/<int:id>',views.editdata),
    path('subcatbycat',views.subcatbycat),
]