from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('AdminProduct',views.viewdata),
    path('adddata2',views.adddata),
    path('addProductUsingApi',views.addProductUsingApi),
    path('deletedata2/<int:id>',views.deletedata),
    
    path('editdata2/<int:id>',views.editdata)
]
