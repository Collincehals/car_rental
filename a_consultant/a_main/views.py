from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *

def home(request):
    tripbookingform = TripBookingForm()
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            booked_trip = form.save(commit=False)
            booked_trip.user = request.user
            booked_trip.save()
            messages.success(request, 'Your trip has been booked!')
            return redirect('home')
    featured_cars = Car.objects.all()
    context = {
        'tripbookingform': tripbookingform,
        'featured_cars': featured_cars
    }
    return render(request, 'a_main/home.html', context)


def about(request):
    return render(request, 'a_main/about.html')

def services(request):
    return render(request, 'a_main/services.html')


def projects(request):
    return render(request, 'a_main/services.html')


def cars(request, brand=None):
    if brand:
        cars = Car.objects.filter(brand__slug = brand)
    else:
        cars = Car.objects.all()
    """
    if request.htmx:
        if 'lamborghini' in request.GET:
            cars = Car.objects.filter(brand__slug = 'lamborghini')
        elif 'landrover' in request.GET:
            cars = Car.objects.filter(brand__slug = 'landrover')  
        elif 'audi' in request.GET:
            cars = Car.objects.filter(brand__slug = 'audi') 
        elif 'mercedes' in request.GET:
            cars = Car.objects.filter(brand__slug = 'mercedes')
        else:
            cars = Car.objects.all() 
       """       
    categories = Brand.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'page': page,
        }
    return render(request, 'a_main/car.html', context)


def car_details(request, pk):
    car_to_view = get_object_or_404(Car, pk=pk)
    related_cars = Car.objects.filter(brand__in=car_to_view.brand.all()).exclude(id=pk)[:6]
    context = {
        'car_to_view':car_to_view,
        'related_cars': related_cars
    }
    return render(request, 'a_main/car-single.html',context)


@login_required
def create_car_post(request):
    carpostform  = CarPostForm()
    if request.method == 'POST':
        form = CarPostForm(request.POST, request.FILES)
        if form.is_valid():
            car= form.save(commit=False) 
            car.owner= request.user
            car.save()
            form.save_m2m()
            messages.success(request, 'Car successfully posted')
            return redirect('cars')
    return render(request, 'a_main/postcreateform.html', {'carpostform': carpostform})


def delete_car(request, pk):    
    if request.method == 'POST':
        car = get_object_or_404(Car, id=pk).delete()
        messages.success(request, 'Car post successfully deleted')
        return redirect('cars')
    return render(request, 'a_main/car_delete.html')
 
    
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