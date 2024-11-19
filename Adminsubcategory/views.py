from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import SubcatModel
from AdminCategory.models import CategoryModel

# Create your views here.
def viewdata(request):
    data=SubcatModel.objects.all()
    context ={
        "subcategory":data
    }
    return render(request,"Subcategory.html",context)

def adddata(request):
    if request.method == "GET":
        # Fetch all categories from CategoryModel
        catdata = CategoryModel.objects.all()
        context = {
            "subcategory": catdata
        }
        return render(request, "addsubcategory.html", context)
    
    else:
        # Get the selected category ID from the form
        cid = request.POST.get("parentCategory")
        catobj = CategoryModel.objects.get(cat_id=cid)
        
        # Upload the image
        cat_image = request.FILES['subcategoryImage']
        fs = FileSystemStorage()
        file = fs.save(cat_image.name, cat_image)
        fileurl = fs.url(file)
        
        # Create and save the new Subcategory object
        obj = SubcatModel()
        obj.subcategoryName = request.POST.get("subcategoryName")
        obj.subcategoryImage = fileurl
        obj.cat_id = catobj  # Assign the fetched CategoryModel object
        obj.save()
        
        messages.success(request, "Subcategory Inserted Successfully!")
        return redirect("/AdminSubcategory")
    
def deletedata(request,id):
        obj = SubcatModel.objects.get(subcat_id = id)
        imagename = os.path.basename(obj.subcategoryImage)
        os.remove(os.path.join(settings.MEDIA_ROOT,imagename))
        obj.delete()
        messages.success(request,"SubCategory Deleted Successfully!")
        return redirect("/AdminSubcategory")

    
def editdata(request,id):
    if request.method == "GET":
        data = SubcatModel.objects.get(subcat_id = id)
        catdata =CategoryModel.objects.all()
        context ={
            "subcategory":data,
            "catdata":catdata
        }
        return render(request,"editsubcategory.html",context)
    else:  
        obj = SubcatModel.objects.get(subcat_id = id)
        cid = request.POST.get("categories")
        catobj = CategoryModel.objects.get(cat_id = cid)
        obj.cat_id = catobj
        obj.subcategoryName = request.POST.get("subcategoryName")
        if 'subcategoryImage' in request.FILES:
            #Delete
            imagename = os.path.basename(obj.subcategoryImage)
            os.remove(os.path.join(settings.MEDIA_ROOT,imagename))
            #Upload
            cat_image = request.FILES['subcategoryImage']
            fs = FileSystemStorage()
            file = fs.save(cat_image.name, cat_image)
            fileurl = fs.url(file)
            obj.subcategoryImage = fileurl
        obj.save()
        messages.success(request,"Subcate Updated Successfully!")
        return redirect("/AdminSubcategory")
    
@csrf_exempt  
def subcatbycat(request):
    cid = request.POST.get("cid")
    subcatdata = SubcatModel.objects.filter(cat_id = cid).values()
    subcatdata = list(subcatdata)
    return JsonResponse(subcatdata,safe=False)


    
# cart --- cart_id,user_id,qty,product_id,price