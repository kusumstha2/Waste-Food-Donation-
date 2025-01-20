from django.contrib import admin
from .models import Donation, Recipient,Donor

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['get_donor_name', 'get_recipients', 'number', 'foodName', 'food_type', 'foodImage', 'food_id', 'quantity', 'description', 'expiry_date', 'created_at', 'latitude', 'longitude']
    search_fields = ['number', 'foodName']
    list_filter = ['food_type']
    list_per_page = 10

    def get_donor_name(self, obj):
        return obj.donor.username if obj.donor else "Unknown"
    get_donor_name.admin_order_field = 'donor'  
    get_donor_name.short_description = 'Donor Name'

    def get_recipients(self, obj):
        # Return a string of recipient names separated by commas
        return ", ".join([recipient.name for recipient in obj.recipients.all()])
    get_recipients.short_description = 'Recipients'


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

    
    
