from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('book_trip/', home, name='book_trip'),
    path('about/', about, name='about'),
    path('services', services, name='services'),
    path('projects/', projects, name='projects'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('cars/', cars, name='cars'),
    path('car/<pk>/', car_details, name='car-details'),
    path('category/<brand>', cars, name='category_page'),
    path('delete/car/<pk>', delete_car, name='delete_car'),
    path('createpost/', create_car_post, name='create_car_post'),
    path('blog/', blog, name='blog'),
    path('pricing/', pricing, name='pricing'),
    path('careers/', careers, name='careers'),
]