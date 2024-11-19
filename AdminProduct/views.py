from django.shortcuts import render,redirect
from .models import ProductModel
from AdminCategory.models import CategoryModel
from Adminsubcategory.models import SubcatModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
def viewdata(request):
    data=ProductModel.objects.all()
    
    context ={
        "products":data
        
        
    }
    return render(request,"product.html",context)

def adddata(request):
    if request.method == "GET":
        data=ProductModel.objects.all()
        catdata=CategoryModel.objects.all()
        context ={
        "products":data,
        "category":catdata,
        
    }
        return render(request,"addproduct.html",context)
    else:
        sid = request.POST.get("subcat")
        subcatobj = SubcatModel.objects.get(subcat_id  = sid)
        #upload
        pro_image1 = request.FILES['image1']
        fs = FileSystemStorage()
        file = fs.save(pro_image1.name, pro_image1)
        fileurl = fs.url(file)
        pro_image2 = request.FILES['image2']
        fs = FileSystemStorage()
        file = fs.save(pro_image2.name, pro_image2)
        fileurl2 = fs.url(file)
        pro_image3 = request.FILES['image3']
        fs = FileSystemStorage()
        file = fs.save(pro_image3.name, pro_image3)
        fileurl3 = fs.url(file)
        
        obj = ProductModel()
        obj.title = request.POST.get("title")
        obj.descriptions = request.POST.get("descriptions")
        obj.price = request.POST.get("retailprice")
        obj.sellPrice = request.POST.get("sellPrice")
        obj.videoUrl = request.POST.get("videoUrl")
        obj.isActive = request.POST.get("isActive")
        obj.subcat_id = subcatobj
        obj.image1 =fileurl
        obj.image2 =fileurl2
        obj.image3 =fileurl3
        
        obj.save()
        messages.success(request,"Product Inserted Successfully!")

        return redirect("/AdminProduct")

    
def deletedata(request,id):
    obj = ProductModel.objects.get(productId = id)
    imagename1 = os.path.basename(obj.image1)
    imagename2 = os.path.basename(obj.image2)
    imagename3 = os.path.basename(obj.image3)
    os.remove(os.path.join(settings.MEDIA_ROOT,imagename1))
    os.remove(os.path.join(settings.MEDIA_ROOT,imagename2))
    os.remove(os.path.join(settings.MEDIA_ROOT,imagename3))
    obj.delete()
    messages.success(request,"Product Deleted Successfully!")
    return redirect("/AdminProduct")

   
def editdata(request,id):
    if request.method == "GET":
        data = ProductModel.objects.get(productId = id)
        catdata=CategoryModel.objects.all()
        context ={
            "product":data,
            "category":catdata
            
        }
        return render(request,"editproduct.html",context)
    else:  
        sid = request.POST.get("subcat")
        subcatobj = SubcatModel.objects.get(subcat_id  = sid)
        obj = ProductModel.objects.get(productId = id)
        obj.title = request.POST.get("title")
        obj.descriptions = request.POST.get("descriptions")
        obj.price = request.POST.get("price")
        obj.sellPrice = request.POST.get("sellPrice")
        obj.videoUrl = request.POST.get("videoUrl")
        obj.isActive = request.POST.get("isActive")
        obj.subcat_id = subcatobj
        if 'image1' in request.FILES:
            #Delete
            imagename1 = os.path.basename(obj.image1)
            os.remove(os.path.join(settings.MEDIA_ROOT,imagename1))
            #Upload
            pro_image1 = request.FILES['image1']
            fs = FileSystemStorage()
            file = fs.save(pro_image1.name, pro_image1)
            fileurl = fs.url(file)
            obj.image1 = fileurl
        if 'image2' in request.FILES:
            #Delete
            imagename2 = os.path.basename(obj.image2)
            os.remove(os.path.join(settings.MEDIA_ROOT,imagename2))
            #Upload
            pro_image2 = request.FILES['image3']
            fs = FileSystemStorage()
            file = fs.save(pro_image2.name, pro_image2)
            fileurl = fs.url(file)
            obj.image2 = fileurl
        if 'image3' in request.FILES:
            #Delete
            imagename3 = os.path.basename(obj.image3)
            os.remove(os.path.join(settings.MEDIA_ROOT,imagename3))
            #Upload
            pro_image3 = request.FILES['image3']
            fs = FileSystemStorage()
            file = fs.save(pro_image3.name, pro_image3)
            fileurl = fs.url(file)
            obj.image3 = fileurl
        obj.save()
        messages.success(request,"product Updated Successfully!")
        return redirect("/AdminProduct")
    

@api_view(['POST'])   
def addProductUsingApi(request):
    try:
        sid = request.POST.get("subcat")
        subcatobj = SubcatModel.objects.get(subcat_id  = sid)
        #upload
        pro_image1 = request.FILES['image1']
        fs = FileSystemStorage()
        file = fs.save(pro_image1.name, pro_image1)
        fileurl = fs.url(file)
        pro_image2 = request.FILES['image2']
        fs = FileSystemStorage()
        file = fs.save(pro_image2.name, pro_image2)
        fileurl2 = fs.url(file)
        pro_image3 = request.FILES['image3']
        fs = FileSystemStorage()
        file = fs.save(pro_image3.name, pro_image3)
        fileurl3 = fs.url(file)
        
        obj = ProductModel()
        obj.title = request.POST.get("title")
        obj.descriptions = request.POST.get("descriptions")
        obj.price = request.POST.get("retailprice")
        obj.sellPrice = request.POST.get("sellPrice")
        obj.videoUrl = request.POST.get("videoUrl")
        obj.isActive = request.POST.get("isActive")
        obj.subcat_id = subcatobj
        obj.image1 =fileurl
        obj.image2 =fileurl2
        obj.image3 =fileurl3
    
        obj.save()
        return JsonResponse({"status":True,"message":"Product Inserted Successfully!"},status=201)
    except Exception as e:
        return JsonResponse({"status":False,"message":"Something Goes wrong!"},status=200)