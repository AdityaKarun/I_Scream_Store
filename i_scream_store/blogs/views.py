from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages 

@login_required(login_url="blogs_signin")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def blogs_home(request):
    return render(request, "blogs/blogs_home.html")

def blogs_signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}!")
            return redirect("blogs_home")
        
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("blogs_signin")

    return render(request, "blogs/blogs_signin.html")

def blogs_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email Already Registered!")
            return redirect("blogs_signup")
        
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully, Please Sign In!")
        return redirect('blogs_signin')

    return render(request, "blogs/blogs_signup.html")

@login_required(login_url="blogs_signin")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def blogs_signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("blogs_signin")