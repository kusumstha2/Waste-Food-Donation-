from django.contrib import admin
from .models import FoodDonation, Recipient,Donor

from django.contrib import admin
from .models import FoodDonation

@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'food_name', 'food_type', 'expiry_date', 'location')
    search_fields = ('donor_name', 'food_name', 'location')
    list_filter = ('food_type', 'expiry_date')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude', 'contact_number', 'address', 'is_veg_preferred', 'preferred_quantity', 'created_at']
    search_fields = ['name', 'contact_number']
    list_filter = ['address', 'is_veg_preferred']
    list_per_page = 10

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude','quantity_kg','food_type']
    search_fields = ['name',]
    list_filter = ['food_type',]
    list_per_page = 10
    
from django.contrib import admin
from .models import ContactUs

# Customize the admin display for the ContactUs modelfrom django.contrib import admin

from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('name',)

admin.register(ContactUs)