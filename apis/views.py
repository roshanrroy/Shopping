from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from rest_framework import viewsets
from Location.models import StatesModel,CityModel
from .serializers import StateSerializer,CitySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
  
from django.core.mail import EmailMultiAlternatives

# 200-299 -  ok response - 
# 300-399 -  Resouce Move/Redirection
# 400-499 - Not Found
# 500-599 - Server

# Get all data  200
# Insert - server resource created - 201
# Delete - Server no return - 204
# No record or data found - 404

class StateViewSet(viewsets.ModelViewSet):
    queryset = StatesModel.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer

@api_view(['GET'])
def getAllState(reqeust):
    try:
        data = StatesModel.objects.all().values()
        states = list(data)
        return JsonResponse(states,safe=False)
    except Exception as e:
        return JsonResponse({"status":False,"message":"Something Goes wrong!"},status=200)

@api_view(['POST'])
def insertState(request):
    try:
        statename = request.POST.get("statename")
        if not StatesModel.objects.filter(statename = statename).exists():
            obj = StatesModel()
            obj.statename = statename
            obj.save()
            return JsonResponse({"status":True,"message":"State Inserted Successfully!"},status=201)
        else:
            return JsonResponse({"status":False,"message":"State Already exist!"},status=201)
    except Exception as e:
        return JsonResponse({"status":False,"message":"Something Goes wrong!"},status=200)


@api_view(['POST'])
def insertStateUsingJson(request):
    try:
        statename = request.data.get("sname")
        if not StatesModel.objects.filter(statename = statename).exists():
            obj = StatesModel()
            obj.statename = statename
            obj.save()
            return JsonResponse({"status":True,"message":"State Inserted Successfully!"},status=201)
        else:
            return JsonResponse({"status":False,"message":"State Already exist!"},status=201)
    except Exception as e:
        return JsonResponse({"status":False,"message":"Something Goes wrong!"},status=200)

@api_view(['DELETE'])
def deleteState(request):
    try:
        state_id = request.data.get("state_id")
        
        if StatesModel.objects.filter(state_id=state_id).exists():
            StatesModel.objects.filter(state_id=state_id).delete()
            return JsonResponse({"status": True, "message": "State deleted successfully!"}, status=204)
        else:
            return JsonResponse({"status": False, "message": "State does not exist!"}, status=404)
    except Exception as e:
      return JsonResponse({"status": False, "message": "Something went wrong!"}, status=500)

@api_view(['DELETE'])
def deleteStatePara(request,id):
    try:
        state_id = id
        
        if StatesModel.objects.filter(state_id=state_id).exists():
            StatesModel.objects.filter(state_id=state_id).delete()
            return JsonResponse({"status": True, "message": "State deleted successfully!"}, status=204)
        else:
            return JsonResponse({"status": False, "message": "State does not exist!"}, status=404)
    except Exception as e:
      return JsonResponse({"status": False, "message": "Something went wrong!"}, status=500)
    

@api_view(['PATCH'])
def updateStatePara(request, id):
    try:
        obj = StatesModel.objects.get(state_id=id)
        obj.statename = request.data.get("sname")
        obj.save()
        return JsonResponse({"status": True, "message": "State updated successfully!"}, status=200)
    except Exception as e:
      return JsonResponse({"status": False, "message": "Something went wrong!"}, status=500)


@api_view(['POST'])
def clogin(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return JsonResponse({"status": False,"message": "Email and password are required"}, status=400)

    user = authenticate(request, username=email, password=password)

   
    if user is not None:
        data = {
            "id":user.id,
            "name":user.first_name,
            "email":user.email
        }
        return JsonResponse({"status": True,"message": "Login successful","userdata":data}, status=200)
    else:
        return JsonResponse({"status": False,"message": "Invalid email or password"}, status=401)
    



@api_view(['POST'])
def checkregistration(request):
    urname = request.data.get("urname")
    email = request.data.get("email")
    password = request.data.get("password")

 
    if not urname or not email or not password:
        return JsonResponse({"status": False,"message": "All fields are required (urname, email, password)"}, status=400)

  
    if User.objects.filter(username=email).exists():
        return JsonResponse({"status": False ,"message": "Email is already registered"}, status=409)

    
    try:
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = urname
        user.save()
    except Exception as e:
        return JsonResponse({"status": False ,"error": "User creation failed", "details": str(e)}, status=500)


    subject = 'Welcome to My App'
    from_email = 'your-email@example.com'
    to_email = [email]

    text_content = f"Hi {urname},\n\nThank you for registering at My App.\nWe are excited to have you on board!"

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
        <div style="text-align: center; padding: 10px; background-color: #f4f4f4; border-bottom: 2px solid #ccc;">
            <img src="https://yourapp.com/static/logo.png" alt="My App Logo" style="width: 150px;">
        </div>
        <div style="padding: 20px;">
            <h2 style="color: #2c3e50;">Hi {urname},</h2>
            <p>Thank you for registering at <strong>My App</strong>. We are excited to have you on board!</p>
            <p style="padding: 10px 0; color: #16a085;">Feel free to <a href="http://127.0.0.1:8000/login" style="color: #2980b9; text-decoration: none;">log in</a> to start using our services.</p>
            <br>
            <p style="font-size: 14px; color: #7f8c8d;">Best Regards,<br>My App Team</p>
        </div>
        <div style="background-color: #f4f4f4; padding: 10px; text-align: center; font-size: 12px; color: #7f8c8d;">
            <p>&copy; 2024 My App. All Rights Reserved.</p>
        </div>
    </body>
    </html>
    """

    email_message = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email_message.attach_alternative(html_content, "text/html")  

    try:
        email_message.send()  
    except Exception as e:
        return JsonResponse({"status": False,"message": "Failed to send confirmation email", "details": str(e)}, status=500)

    return JsonResponse({"status": True ,"message": "Registration successful! A confirmation email has been sent."}, status=201)
