from django.shortcuts import render,redirect
from .models import User,Profile
from django.contrib import messages 
from django.core.validators import validate_email
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        errors = False
        if not username:
            messages.error(request,"Please fill username")
            errors = True
            return render(request,'register.html')
            
        
        if not email:
            messages.error(request,"Please fill email")
            return render(request,'register.html')
        
        if not password:
            messages.error(request,"Please fill password")
            return render(request,'register.html')
        
        if errors:
            return render(request,'register.html',{'username':username})
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist.")
            return redirect('register')
        
        if len(password) < 4:
            messages.error(request,'Password must be contain more than 4 characters.')
        
        try:
            validate_email(email)
        except Exception as e:
            messages.error(request,"invalid email")
        
        user_obj = User.objects.create(username = username, email = email, password = password)
        user_obj.set_password(password)
        user_obj.save()        
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
    
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
    
        if not username:
           messages.error(request,"Please fill username.")
           return render(request,'login.html')
    
        if not password:
            messages.error(request,"Please fill password.")
            return render(request,'login.html')
    
        user = authenticate(username = username, password = password)
    
        if user is not None:
            login(request,user) 
            return redirect('index')
        
        else:
            messages.error(request,"Invalid credientials")
            return redirect('login')
        
    return render(request,'login.html')

def user_profile(request):
    user= request.user
    user_profile = Profile.objects.get(user = user)
    orders = user.orders.all()
    return render(request,'profile.html',{'user_profile':user_profile,'orders':orders})



def update_profile_picture(request):
    if request.method == 'POST':
        if 'profile_pic' in request.FILES:
            profile = request.user.user_profile
            profile.profile_picture = request.FILES['profile_pic']
            profile.save()
            return redirect('profile')
    return redirect('profile')

def user_logout(request):
    logout(request)
    return redirect('login')



    
            
                        
        
        
            