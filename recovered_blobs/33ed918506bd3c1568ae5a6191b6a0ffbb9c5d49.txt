from rest_framework import serializers
from .models import *

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDonation
        fields = '__all__'
        
class RecipientSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True, read_only=True) 
    class Meta:
        model = Recipient
        fields = '__all__'
               
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Donor
        fields = '__all__'               
        