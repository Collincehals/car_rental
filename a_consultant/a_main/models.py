from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    brand = models.ManyToManyField('Brand', related_name='brands')
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='cars', blank=False, null=False)
    hire_rate_hour = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    hire_rate_day = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    lease_rate = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    mileage = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    transmission = models.CharField(max_length=400, null=True, blank=True, choices = [('manual', 'manual'),('automatic', 'automatic')])
    seats = models.IntegerField( null=True, blank=True)
    luggage = models.IntegerField(null=True, blank=True)
    fuel = models.CharField(max_length=400, null=True, blank=True, choices=[('petrol', 'petrol'),('diesel','diesel'),('electric','electric')])
    description = models.CharField(max_length=400, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, unique=True)
    
    def __str__(self):
        brands = ', '.join([brand.name for brand in self.brand.all()])
        return f'{brands}: {self.name}'
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
    
    PICK_UP_LOCATION_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Kiambu', 'Kiambu'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Kericho', 'Kericho'),
        ('Bungoma', 'Bungoma'),
    ]
    
    DROP_OFF_LOCATION_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Kiambu', 'Kiambu'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Kericho', 'Kericho'),
        ('Bungoma', 'Bungoma'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_up_location = models.CharField(max_length=200, choices=PICK_UP_LOCATION_CHOICES,blank=False, null=True)
    drop_off_location = models.CharField(max_length=200, choices=DROP_OFF_LOCATION_CHOICES,blank=False, null=True)
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
 
        

class CarRental(models.Model):
    RENTAL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    
    PICK_UP_LOCATION_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Kiambu', 'Kiambu'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
    ]
    
    DROP_OFF_LOCATION_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Kiambu', 'Kiambu'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
    ]
     

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    pick_up_time= models.TimeField(max_length=200, blank=False, null=True)
    status = models.CharField(max_length=20, choices=RENTAL_STATUS_CHOICES, default='pending')
    pick_up_location = models.CharField(max_length=200, choices=PICK_UP_LOCATION_CHOICES,blank=False, null=True)
    drop_off_location = models.CharField(max_length=200, choices=DROP_OFF_LOCATION_CHOICES,blank=False, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    renting_id = models.CharField(max_length=200, default = uuid.uuid4, primary_key=True, unique=True, null=False) 

    def __str__(self):
        return f"Rental ID: {self.renting_id} - {self.car} - {self.customer}"   
    class Meta:
        ordering = ['-date_ordered']
        
        
class Bookmark(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_bookmarked = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, default=uuid.uuid4, primary_key=True)
    
    def __str__(self):
        return f'{self.customer.username}:{self.bookmark}'
    class Meta:
        ordering = ['-date_bookmarked']