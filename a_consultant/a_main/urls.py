from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services', services, name='services'),
    path('projects/', projects, name='projects'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('cars/', cars, name='cars'),
    path('blog/', blog, name='blog'),
    path('pricing/', pricing, name='pricing'),
    path('careers/', careers, name='careers'),
]