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
    
class Donation(models.Model):
    VEGETARIAN = 'veg'
    NON_VEGETARIAN = 'nonveg'

    FOOD_TYPE_CHOICES = [
        (VEGETARIAN, 'Vegetarian'),
        (NON_VEGETARIAN, 'Non-Vegetarian')
    ]
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    recipients = models.ManyToManyField('Recipient', related_name='allocated_donations', blank=True)
    number = models.CharField(max_length=50)
    foodName = models.CharField(max_length=191)
    food_type = models.CharField(max_length=6, choices=FOOD_TYPE_CHOICES)
    foodImage = models.ImageField(upload_to='images/', null=True, blank=True)
    food_id = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
   
    def __str__(self):
        return f"{self.foodName} by {self.donor.username}"

class Donor(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()  # Latitude
    longitude= models.FloatField()  # Longitude
    food_type = models.CharField(max_length=255)
    quantity_kg = models.FloatField()
    

    
    