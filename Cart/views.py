from django.shortcuts import render, redirect, get_object_or_404
from AdminCategory.models import CategoryModel
from AdminProduct.models import ProductModel
from Product.models import CartModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def cart(request):
    cartdata = CartModel.objects.filter(user_id=request.user.id)

    # Calculate the subtotal (sum of total price for all products)
    subtotal = sum(item.total_price for item in cartdata)

    context = {
        "cartdata": cartdata,
        "subtotal": subtotal,  # Pass subtotal to template
    }
    return render(request, "cart.html", context)


def delete_cart_item(request, cart_id):
    """Delete a cart item by its cart_id."""
    cart_item = get_object_or_404(CartModel, cart_id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('/cart') 

@csrf_exempt  
def loadcart(request):
    cartdata = CartModel.objects.filter(user_id=request.user.id)
    subtotal = sum(item.total_price for item in cartdata)
    data = []
    for row in cartdata:
        data.append({
            "cart_id":row.cart_id,
            "product_name":row.productId.title,
            "product_image":row.productId.image1,
            "qty":row.qty,
            "price":row.price,
            "total_price": row.total_price
        })
    return JsonResponse({"cartdata":data,"subtotal":subtotal},safe=False)