from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
def home(request):
    return render(request, 'a_main/home.html')

def about(request):
    return render(request, 'a_main/about.html')

def services(request):
    return render(request, 'a_main/services.html')

def projects(request):
    return render(request, 'a_main/services.html')

def cars(request):
    cars = Car.objects.all()
    categories = Brand.objects.all()
    context = {
        'cars': cars, 
        'categories': categories,
        }
    return render(request, 'a_main/car.html', context)


def create_car_post(request):
    carpostform  = CarPostForm()
    if request.method == 'POST':
        form = CarPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('cars')
    return render(request, 'a_main/postcreateform.html', {'carpostform': carpostform})
    
    
    
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