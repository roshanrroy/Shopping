from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Location.models import StatesModel
from Location.models import CityModel
from Product.models import CartModel
from .models import OrderModel
from django.utils.timezone import now
from Item.models import ItemModel
from AdminProduct.models import ProductModel
import razorpay
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
def checkout(request):
    cartdata = CartModel.objects.filter(user_id=request.user.id)
    subtotal = sum(item.total_price for item in cartdata)
    data=CityModel.objects.all()
    statedata = StatesModel.objects.all()
    context ={
    "statedata":statedata,
    "cartdata": cartdata,
    "subtotal": subtotal,  
        }
    return render(request,"checkout.html",context)

@login_required
def create_order(request):
    if request.method == 'POST':
        amount = float(request.POST.get('finaltotal')) * 100  # Amount in paisa
        order_currency = 'INR'
        
        order = client.order.create({
            'amount': amount,
            'currency': order_currency, 
            'payment_capture': '1'
        })
        
        context = {
            'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
            'amount': amount,
            'currency': order_currency,
            'order_id': order['id'],
            'callback_url': '/order_entry',
            "name":request.POST.get("name"),
            "email":request.POST.get("email"),
            "mobile":request.POST.get("mobile"),
            "address1":request.POST.get("address1"),
            "address2":request.POST.get("address2"),
            "city":request.POST.get("city"),
            "finaltotal":request.POST.get("finaltotal"),
        }

        return render(request, 'payment.html', context)
        
@login_required
def order_entry(request):
    if request.method == 'POST':
        obj = OrderModel()
        obj.user = request.user
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.mobile=request.POST.get("mobile")
        obj.address_line1=request.POST.get("address1")
        obj.address_line2=request.POST.get("address2")
        obj.finaltotal= request.POST.get("finaltotal")

        city_id = request.POST.get("city")
        obj.city_id = CityModel.objects.get(city_id=city_id) if city_id else None
        
        obj.orderdatetime = now()
        obj.save()

        #item
        orderobj = obj
        cartdata = CartModel.objects.filter(user_id=request.user.id)
        for row in cartdata:
            itemobj = ItemModel()
            itemobj.order_id = orderobj
            itemobj.productId = row.productId
            itemobj.qty = row.qty
            itemobj.price = row.price
            itemobj.save()
        CartModel.objects.filter(user_id=request.user.id).delete()
    return redirect('/')
    
