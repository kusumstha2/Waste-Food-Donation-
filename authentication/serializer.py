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
from djoser.serializers import UserCreateSerializer
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      model = User
      fields = '__all__'

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