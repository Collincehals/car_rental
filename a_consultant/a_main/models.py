from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    brand = models.ManyToManyField('Brand', related_name='brands')
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='cars', blank=False, null=False)
    description = models.CharField(max_length=400, null=True, blank=True)
    hire_rate = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return f'{self.brand}: {self.name}'
    class Meta:
        ordering = ['-date_created']

class Brand(models.Model):
    slug = models.SlugField(max_length=20, unique=True)
    name = models.CharField(max_length=50,null=False, blank=False)
    image = models.ImageField(upload_to='brand_images', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
    
    
class TripBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_up_location = models.CharField(max_length=200, blank=False, null=False)
    drop_off_location = models.CharField(max_length=200, blank=False, null=False)
    pick_up_date = models.DateField(max_length=200, blank=False, null=False)
    drop_off_date = models.DateField(max_length=200, blank=False, null=False)
    pick_up_time= models.TimeField(max_length=200, blank=False, null=False)
    booking_number = models.CharField(max_length=200, default = uuid.uuid4, primary_key=True, unique=True, null=False) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}:{self.booking_number}' 
    class Meta:
        ordering = ['-date_created']