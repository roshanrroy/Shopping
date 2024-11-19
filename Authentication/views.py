from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.

def Registration(request):
    if request.method == "GET":
        return render(request, "Registration.html")
    else:
        urname = request.POST.get("urname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the email (username) already exists
        user = User.objects.filter(username=email)
        
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/registration')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = urname
        user.save()

        
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
        email_message.attach_alternative(html_content, "text/html")  # Attach HTML version

    
        email_message.send()  # Send the email
        messages.success(request, "Registration successful! A confirmation email has been sent.")
       

        return redirect("/login")
    
def user_login(request):
    if request.method == "GET":
        return render(request,"Login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            request.session["country"] = "India"
            return redirect("/")
        else:
            messages.info(request, "Username or password not match")
            return redirect("/login")
    


def userlogout(request):
    #cou = request.session.country
    logout(request)
    return redirect("/login")
   
