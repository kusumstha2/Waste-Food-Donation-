from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework  import viewsets,filters
from .serializer import *
from  rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .utils import calculate_distance
from sklearn.neighbors import NearestNeighbors
import numpy as np
from django.http import JsonResponse
from geopy.distance import geodesic
from .models import Recipient
from django.http import JsonResponse
from .utils import notify_recipients
from .utils import calculate_distance, knn_recipients
from django.shortcuts import render





class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_field = ('donor',)
    # permission_classes = (isDonorReadOnly,)
    # authentication_classes = [TokenAuthentication]
  

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = RecipientSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_field = ('name',)
    
class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = RecipientSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend)
    pagination_class=PageNumberPagination
    search_field = ('name',)
    # permission_classes = (isDonorReadOnly,)
    # authentication_classes = [TokenAuthentication]
    # permission_classes=(IsAuthenticated,)
    

    


def some_view(request):
    donor_lat, donor_lon = 27.7172, 85.3240  # Example donor location (Kathmandu)
    recipient_lat, recipient_lon = 27.6751, 85.3354  # Example recipient location

    distance = calculate_distance(donor_lat, donor_lon, recipient_lat, recipient_lon)
    return JsonResponse({
        "donor_location": {"latitude": donor_lat, "longitude": donor_lon},
        "recipient_location": {"latitude": recipient_lat, "longitude": recipient_lon},
        "distance_km": distance
    })
    


def calculate_distance_view(request):
    if request.method == "GET":
        # Parse donor's latitude and longitude from the query parameters
        donor_latitude = float(request.GET.get('latitude'))
        donor_longitude = float(request.GET.get('longitude'))
        
        # Get all recipients from the database
        recipients = Recipient.objects.all()
        
        recipient_distances = []
        
        for recipient in recipients:
            # Calculate distance using geopy
            distance = geodesic((donor_latitude, donor_longitude), 
                                (recipient.latitude, recipient.longitude)).km
            
            # Append recipient details and calculated distance
            recipient_distances.append({
                "name": recipient.name,
                "contact_number": recipient.contact_number,
                "address": recipient.address,
                "distance_km": round(distance, 2),
            })
        
        # Sort recipients by distance (nearest first)
        recipient_distances.sort(key=lambda x: x["distance_km"])
        
        return JsonResponse({"recipients": recipient_distances}, safe=False)
    
    return JsonResponse({"error": "Invalid HTTP method. Use GET."}, status=400)
    
from django.http import JsonResponse
from .models import Donation, Recipient
from .utils import knn_recipients

def knn_recipients_view(request):
    donation_id = request.GET.get('donation_id')
    num_recipients = int(request.GET.get('num_recipients', 5))  # Default to 5 recipients

    if not donation_id:
        return JsonResponse({"error": "donation_id is required"}, status=400)

    try:
        donation = Donation.objects.get(food_id=donation_id)
    except Donation.DoesNotExist:
        return JsonResponse({"error": "Donation not found"}, status=404)

    # Prepare recipient data
    recipients = [
        (recipient.id, (recipient.latitude, recipient.longitude))
        for recipient in donation.recipients.all()
    ]

    # Perform KNN calculation
    nearest_recipients = knn_recipients(
        (donation.latitude, donation.longitude), recipients, num_recipients
    )

    # Build response
    response_data = [{"recipient_id": r} for r in nearest_recipients]
    return JsonResponse({"nearest_recipients": response_data})




# views.py
from django.core.mail import send_mail
from django.conf import settings
from .models import Donation, Recipient
from .utils import calculate_distance, knn_recipients
from django.http import JsonResponse

def notify_recipients(donation_id):
    try:
        donation = Donation.objects.get(pk=donation_id)
        recipients = knn_recipients(donation)  # Assuming this is your KNN function

        # Iterate through the recipients and notify them
        for recipient in recipients:
            # Send email notification (Example)
            send_mail(
                subject=f"New Donation: {donation.foodName}",
                message=f"Hello {recipient.name},\n\nThere is a new donation available: {donation.foodName}. Please contact us if you're interested.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient.contact_number],  # Assuming you have an email or contact field
            )
            # Or notify via SMS if you have an SMS service like Twilio
            # send_sms(recipient.contact_number, "New food donation available!")

        return JsonResponse({"message": "Notifications sent successfully"})

    except Donation.DoesNotExist:
        return JsonResponse({"error": "Donation not found"}, status=404)

