# from django.contrib import admin

# from django.contrib import admin

# # Register your models here.
# from .models import *
# from django.contrib.auth.admin import UserAdmin

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     list_display = ('username','email','first_name','last_name','is_staff','role',)
#     search_fields =('username','email','first_name','last_name',)
#     list_per_page=5


from django.contrib import admin
from .models import *
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#    list_display = ('email','address','phone_number')
#    search_fields = ['email']

# admin.site.register(User,UserAdmin)
admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)
class OTPVerificationAdmin(admin.ModelAdmin):
   list_display = ('email','otp','otp_created_at')

admin.site.register(OTPVerification,OTPVerificationAdmin)
