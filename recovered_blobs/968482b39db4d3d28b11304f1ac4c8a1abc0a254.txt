# from rest_framework import serializers
# from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta :
        
#         fields= (
#            'email', 
#            'username',
#            'role', 'password',
#         )  
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
        
        
#         model = User

from rest_framework import serializers
from .models import *
from .models import Donor,User,Recipient
from rest_framework import serializers
from django.db import transaction
from rest_framework.authtoken.models import Token

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','phone', 'is_Recipient','is_Donor']
        
# class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#       model = User
#       fields = '__all__'

class OTPVerificationSerializer(serializers.ModelSerializer):
   class Meta:
      model = OTPVerification
      fields = '__all__'
   
   def validate_otp(self,value):
      if len(value) != 6:
         raise serializers.ValidationError('OTP must be 6 digits long.')
      return value

class DonorSignupSerializer(serializers.ModelSerializer): 
    re_password = serializers.CharField(style = {"input_type":"password"}, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password', 're_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            address=self.validated_data['address'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],  # Use 'phone' instead of 'phone_number'
        )
        password = self.validated_data['password']
        re_password = self.validated_data['re_password']
        if password != re_password:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_Donor = True
        user.save()
        Donor.objects.create(user=user, phone=user.phone)
        return user

class RecipientSignupSerializer(serializers.ModelSerializer): 
    re_password = serializers.CharField(style = {"input_type":"password"}, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password', 're_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            address=self.validated_data['address'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],  # Use 'phone' instead of 'phone_number'
        )
        password = self.validated_data['password']
        re_password = self.validated_data['re_password']
        if password != re_password:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_Recipient = True
        user.save()
        Recipient.objects.create(user=user, phone=user.phone)
        return user

