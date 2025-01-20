

# # Create your views here.
# from django.shortcuts import render
# # Create your views here.
# from rest_framework import viewsets, filters
# from django_filters import rest_framework as filters
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.exceptions import AuthenticationFailed
# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from .serializer import *
# from foodapp.permission import isDonorReadOnly


# class RegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(serializer.validated_data['password']) 
#             user.save()
#             return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class LoginAPIView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             raise AuthenticationFailed('Both username and password are required')
        
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#         if user:
           
#             if not user.is_active:
#                 raise AuthenticationFailed('User account is inactive')
            
    
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'username': user.username, 'role': user.role})
        
#         raise AuthenticationFailed('Invalid username or password')


# class LogoutAPIView(APIView):
#    permission_classes = [IsAuthenticated]
#    def post(self, request):
#       username = request.data.get('username')
#       password = request.data.get('password')
#       if not(username and password):
#          return Response({'detail':'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
#       user = authenticate(username=username, password=password)
#       if user is not None:
#          logout(request)
#          try:
#             token = Token.objects.get(user=user)
#             token.delete()
#             return Response({'detail': 'Successfully logged out.'})
#          except Token.DoesNotExist:
#             return Response({'detail': 'Token does not exist.'}, status=status.HTTP_404_NOT_FOUND)
#       else:
#          return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets,status
from django.core.mail import send_mail
import random
from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
   
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
# class UserViewset(viewsets.ModelViewSet):
#    queryset = User.objects.all().order_by('email')
#    serializer_class = UserSerializer

class OTPVerificationViewset(viewsets.ModelViewSet):
   queryset = OTPVerification.objects.all().order_by('email')
   serializer_class = OTPVerificationSerializer
   
   @action(detail = False, methods = ['post'], url_path = 'send-otp')
   def send_otp(self,request):
      email = request.data.get('email')
      
      if email:
         otp = random.randint(100000, 999999)
         otp_record,created = OTPVerification.objects.update_or_create(
            email = email,
            defaults = {'otp':str(otp),'otp_created_at':timezone.now()}
         )
         
         send_mail(
            'Your OTP code',
            f'YOur OTP code is {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False
         )
         return Response({"message":"OTP send successfully","otp":otp},status = status.HTTP_200_OK)
      return Response({"error":"Email is required"},status = status.HTTP_400_BAD_REQUEST)
   
   @action(detail=False, methods=['post'],url_path='verify-otp')
   def verify_otp(self,request):
      email = request.data.get('email')
      otp = request.data.get('otp')
      
      if email and otp:
         try:
            otp_record = OTPVerification.objects.get(email = email,otp=otp)
            
            if otp_record.is_expired():
               otp_record.delete()
               return Response({"error":"OTP is expired"},status = status.HTTP_400_BAD_REQUEST)
            
            otp_record.delete()
            return Response({"message":"OTP verified successfully"},status = status.HTTP_200_OK)
         
         except OTPVerification.DoesNotExist:
            return Response({"error":"Invalid OTP"},status = status.HTTP_400_BAD_REQUEST)
      
      return Response ({"error":"Email and OTP are required"},status = status.HTTP_400_BAD_REQUEST)
   


User = get_user_model()
# @csrf_exempt

# def register_view(request):
#     if request.method=='GET':
#       return render(request, 'signup.html')
#     elif  request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')  # Get confirm password
#         name = request.POST.get('name')
#         phone_number = request.POST.get('phone_number')
#         address = request.POST.get('address')
#         img = request.FILES.get('img')  # Handle optional image upload

#         if password != confirm_password:  # Password matching validation
#             messages.error(request, "Passwords do not match.")
#             return render(request, 'signup.html')

#         try:
#             user = User.objects.create_user(
#                 email=email,
#                 password=password,
#                 Name=name,
#                 Phone_Number=phone_number,
#                 Address=address,
#                 Img=img
#             )
#             messages.success(request, "Registration successful!")
#             return redirect('login')  # Redirect to login or any other page
#         except Exception as e:
#             messages.error(request, f"Registration failed: {e}")

#     return render(request, 'signup.html')
   