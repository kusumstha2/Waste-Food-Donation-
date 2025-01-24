from django.contrib import admin

# Register your models here.
from location.models import DonorLocation, RecipientLocation
@admin.register(DonorLocation)
class DonorLocationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'latitude', 'longitude')
    
@admin.register(RecipientLocation)
class RecipientLocationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'latitude', 'longitude')