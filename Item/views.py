from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from Checkout.models import OrderModel
from AdminCategory.models import CategoryModel
from AdminProduct.models import ProductModel  # Adjust the import path as needed
from django.contrib.auth.decorators import login_required
from Item.models import ItemModel
from Product.models import CartModel
import json
from django.contrib.auth.decorators import login_required


# @login_required(login_url="/login")
def order(request):
    data = OrderModel.objects.filter(user_id=request.user.id)
    context={
        "order":data
    }
    return render(request,"order.html",context)

def item(request,order_id):
    items = ItemModel.objects.filter(order_id=order_id)

    # Calculate the subtotal (sum of total price for all products)
    context = {
        "items":items
    }
    return render(request,"item.html",context)



