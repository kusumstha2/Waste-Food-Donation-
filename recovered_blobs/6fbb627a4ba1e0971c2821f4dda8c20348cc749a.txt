from django.db import models
from django.conf import settings
from authentication.models import *
# Create your models here.

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_veg_preferred = models.BooleanField(default=True)  
    preferred_quantity = models.IntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.name
    
from django.db import models

class FoodDonation(models.Model):
    # FOOD_TYPE_CHOICES = [
    #     ('veg', 'Vegetarian'),
    #     ('non-veg', 'Non-Vegetarian'),
    # ]

    donor_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=20)
    food_image = models.ImageField( blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField()
    location = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.food_name} by {self.donor_name}"

class Donor(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()  # Latitude
    longitude= models.FloatField()  # Longitude
    food_type = models.CharField(max_length=255)
    quantity_kg = models.FloatField()
    

from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    

    def __str__(self):
        return f"{self.name} - {self.subject}"
