from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *

def home(request):
    if request.user.is_authenticated:
        tripbookingform = TripBookingForm()
        if request.method == 'POST':
            form = TripBookingForm(request.POST)
            if form.is_valid():
                booked_trip = form.save(commit=False)
                booked_trip.user = request.user
                booked_trip.save()
                messages.success(request, 'Your trip has been booked!')
                return redirect('home')
    else:
        tripbookingform = TripBookingForm()
        
    featured_cars = Car.objects.all()
    cars_total= Car.objects.all().count()
   
    if request.user.is_authenticated:
        bookmarks_count = Bookmark.objects.filter(customer=request.user).count()
    else:
        bookmarks_count = []   
    context = {
        'tripbookingform': tripbookingform,
        'featured_cars': featured_cars,
        'cars_total': cars_total,
        'bookmarks_count': bookmarks_count,
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
    car_list = Car.objects.all()
    paginator = Paginator(car_list, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'a_main/pricing.html', context)


def careers(request):
    return render(request, 'a_main/blog-single.html')

@login_required
def bookmark(request, pk):
    original_car = get_object_or_404(Car, id=pk)
    bookmark = Bookmark(customer=request.user, bookmark=original_car)
    bookmark.save()
    messages.success(request,'Car saved successfully!')
    return redirect('bookmark_view')


def undobookmark(request, pk):
    bookmarked_car = get_object_or_404(Bookmark, id=pk)
    if request.user == bookmarked_car.customer:
        bookmarked_car.delete()
        messages.success(request,'Save undone successfully!')
        return redirect('bookmark_view')
    
    
@login_required
def bookmarkview(request):
    bookmarks = Bookmark.objects.filter(customer=request.user)
    bookmarks_count = Bookmark.objects.filter(customer=request.user).count()
    context = {
        'bookmarks': bookmarks, 
        'bookmarks_count': bookmarks_count,
        }
    return render(request,'a_main/saved_items.html',context)

@login_required
def rent_car(request, pk):
    car_to_rent = get_object_or_404(Car, pk=pk)
    car_rent_form = CarRentalForm()
    if request.method == 'POST':
        form = CarRentalForm(request.POST)
        if form.is_valid():
            rented_car = form.save(commit=False)
            rented_car.name = car_to_rent.name
            rented_car.customer = request.user
            rented_car.car = car_to_rent
            rented_car.save()
            print('Rented Car:',rented_car)
            messages.success(request, 'Car rental request sent!Check your email for details.')
            return redirect('cars')
    context = {
        'car_to_rent':car_to_rent,
        'car_rent_form':car_rent_form,
    }
    return render(request, 'a_main/car_renting_form.html', context)


