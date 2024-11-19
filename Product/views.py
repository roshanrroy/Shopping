from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import CartModel
from AdminCategory.models import CategoryModel
from AdminProduct.models import ProductModel  # Adjust the import path as needed
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
def product(request):
    data = ProductModel.objects.all()
    context={
        "products":data
    }
    return render(request,"CoustomProduct.html",context)


def detail(request,id):
    data = ProductModel.objects.get(productId = id)
    context ={
            "product":data,
        }
    return render(request,"detail.html",context)

@login_required  
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        price = request.POST.get('product_price')
        qty = request.POST.get('qty')

        try:
            qty = int(qty) 
        except ValueError:
            qty = 1

        productobj = ProductModel.objects.get(productId = product_id)
        cart_item = CartModel.objects.filter(user=request.user, productId=productobj).first()
        if cart_item:  
            cart_item.qty += qty 
            cart_item.save()
        else:
            obj  = CartModel()
            obj.user = request.user
            obj.productId = productobj
            obj.qty = qty
            obj.price = price
            obj.save()


        
    return redirect('/')