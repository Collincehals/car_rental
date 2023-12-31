from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services', services, name='services'),
    path('projects/', projects, name='projects'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('project/page/', project_page, name='project_page'),
    path('blog/', blog, name='blog'),
    path('pricing/', pricing, name='pricing'),
    path('careers/', careers, name='careers'),
]