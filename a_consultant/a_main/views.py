from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'a_main/home.html')

def about(request):
    return render(request, 'a_main/about.html')

def services(request):
    return render(request, 'a_main/services.html')

def projects(request):
    return render(request, 'a_main/services.html')

def cars(request):
    return render(request, 'a_main/car.html')

def project_page(request):
    return render(request, 'a_main/car_single.html')

def portfolio(request):
    return render(request, 'a_main/about.html')

def contact(request):
    return render(request, 'a_main/contact.html')

def blog(request):
    return render(request, 'a_main/blog.html')

def pricing(request):
    return render(request, 'a_main/pricing.html')

def careers(request):
    return render(request, 'a_main/blog-single.html')