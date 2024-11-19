from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StatesModel
from .models import CityModel
# Create your views here.
def state(request):
    if request.method == "GET":
        data=StatesModel.objects.all()
        # countrydata =CountryModel.objects.all()
        context ={
        "states":data
        
    }
        return render(request,"state.html",context)
    else:
        obj = StatesModel()
        obj.statename=request.POST.get("statename")
        obj.save()
        messages.success(request,"State Inserted Successfully!")


        return redirect("/state")
    
def city(request):
    if request.method == "GET":
        data=CityModel.objects.all()
        statedata = StatesModel.objects.all()
        context ={
        "city":data,
        "statedata":statedata
    }
        return render(request,"city.html",context)
    else:
        sid = request.POST.get("state")
        stateobj = StatesModel.objects.get(state_id = sid)
        obj = CityModel()
        obj.cityname=request.POST.get("cityname")
        obj.state_id = stateobj
        obj.save()
        messages.success(request,"City Inserted Successfully!")


        return redirect("/city")  
    
@csrf_exempt  
def citybystate(request):
    sid = request.POST.get("sid")
    citydata = CityModel.objects.filter(state_id = sid).values()
    citydata = list(citydata)
    return JsonResponse(citydata,safe=False)
    
   
