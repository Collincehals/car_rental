from django.db import models
import uuid
# Create your models here.
class Car(models.Model):
    brand = models.ManyToManyField('Category', related_name='brands')
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='cars', blank=False, null=False)
    description = models.CharField(max_length=400, null=True, blank=True)
    hire_rate = models.DecimalField(null=False, blank=False, max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return f'{self.brand}: {self.name}'
    class Meta:
        ordering = ['-date_created']

class Category(models.Model):
    slug = models.SlugField(max_length=20, unique=True)
    name = models.CharField(max_length=50,null=False, blank=False)
    image = models.ImageField(upload_to='brand_images', blank=True, null=True)
    
    def __str__(self):
        return f'{self.slug}:{self.name}'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
        