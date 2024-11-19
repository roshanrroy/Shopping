from django.shortcuts import render,redirect
from .models import CategoryModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# Create your views here.
def viewdata(request):
    data=CategoryModel.objects.all()
    context ={
        "category":data
    }
    return render(request,"Category.html",context)

def adddata(request):
    if request.method == "GET":
        return render(request,"Addcategory.html")
    else:
        #upload
        cat_image = request.FILES['categoryImage']
        fs = FileSystemStorage()
        file = fs.save(cat_image.name, cat_image)
        fileurl = fs.url(file)
        obj = CategoryModel()
        obj.categoryName=request.POST.get("categoryName")
        obj.categoryImage = fileurl
        obj.save()
        messages.success(request,"Categories Inserted Successfully!")
        return redirect("/Admincategory")
    
def deletedata(request,id):
    obj = CategoryModel.objects.get(cat_id = id)
    imagename = os.path.basename(obj.categoryImage)
    os.remove(os.path.join(settings.MEDIA_ROOT,imagename))
    obj.delete()
    messages.success(request,"Category Deleted Successfully!")
    return redirect("/Admincategory")

def editdata(request,id):
    if request.method == "GET":
        data = CategoryModel.objects.get(cat_id = id)
        context = {
            "category":data
        }
        return render(request,"editcategory.html",context)
    else:
        obj = CategoryModel.objects.get(cat_id = id)
        obj.categoryName=request.POST.get("categoryName")
        if 'categoryImage' in request.FILES:
            #Delete
            imagename = os.path.basename(obj.categoryImage)
            os.remove(os.path.join(settings.MEDIA_ROOT,imagename))
            #Upload
            cat_image = request.FILES['categoryImage']
            fs = FileSystemStorage()
            file = fs.save(cat_image.name, cat_image)
            fileurl = fs.url(file)
            obj.categoryImage = fileurl
        obj.save()
        messages.success(request,"Category Updated Successfully!")
        return redirect("/Admincategory")
    
    
