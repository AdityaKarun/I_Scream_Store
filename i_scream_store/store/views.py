from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

def careers(request):
    return render(request, 'store/careers.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, "Your message has been sent successfully!")

        return redirect('contact')

    return render(request, 'store/contact.html')