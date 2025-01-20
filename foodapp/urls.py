from django.urls import path, include
from rest_framework import routers
from .views import *
from .views import calculate_distance_view
from .views import notify_recipients
from .views import knn_recipients


router = routers.SimpleRouter()
router.register(r'donations', DonationViewSet,basename='donation')
router.register(r'recipients',RecipientViewSet,basename='recipient')
router.register(r'donors',DonorViewSet,basename='donor')

urlpatterns = router.urls+[
    path('calculate-distance/', calculate_distance_view, name='calculate_distance'),
    path('notify-recipients/<int:donation_id>/', notify_recipients, name='notify_recipients'),
    path('knn/', knn_recipients_view, name='knn_recipients'),
 
]

