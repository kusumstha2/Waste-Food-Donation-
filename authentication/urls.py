# from django.urls import path, include
# from django.contrib.auth.models import User
# from .views import LoginAPIView,LogoutAPIView,RegistrationAPIView


# urlpatterns = [
#    path('register/',RegistrationAPIView.as_view(),name='user-registration'),
#    path('login/',LoginAPIView.as_view(),name='user-login'),
#    path('logout/',LogoutAPIView.as_view(),name= 'user-logout'),
   
# ]

from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

# router.register(r'user',UserViewset,basename='user')
router.register(r'otp-verification',OTPVerificationViewset,basename='otp-verification')

urlpatterns = [
   path('', include(router.urls)),
   # path('signup/',register_view),
   path('auth/',include('djoser.urls')),
   path('auth/',include('djoser.urls.authtoken')),
   path('auth/', include('djoser.urls.jwt')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
