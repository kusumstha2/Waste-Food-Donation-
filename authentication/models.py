# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.utils import timezone

# # Custom User Manager
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email.lower())
#         extra_fields.pop("confirm_password", None)  
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)  # Ensure active status for superuser
#         return self.create_user(email, password, **extra_fields)

# # Custom User Model
# class User(AbstractUser):
    
#     username=None
#     name=models.CharField(max_length=250,null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=10, null=True, blank=True)
#     email = models.EmailField(unique=True)
#     img = models.ImageField(upload_to='UserImage/', null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name", "img",  "phone_number", "address"]
    
#     objects = CustomUserManager()

    
#     def full_name(self):
#         return self.name  

#     def __str__(self):
#         return self.full_name()
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email.lower())  # Ensure email is lowercase
        extra_fields.pop("confirm_password", None)  # Ensure confirm_password is not saved
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)  # Ensure active status for superuser
        return self.create_user(email, password, **extra_fields)

# Custom User Model
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    # Phone number with RegexValidator
    phone_number = models.CharField(
        max_length=15,  # Allow flexibility in length
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )

    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='UserImage/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "img", "phone_number", "address"]

    objects = CustomUserManager()

    def full_name(self):
        return self.name  

    def __str__(self):
        return self.full_name()


# OTP Verification Model
class OTPVerification(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    otp_created_at = models.DateTimeField(default=timezone.now)

    def is_expired(self):
        expiration_time = self.otp_created_at + timezone.timedelta(minutes=10)
        return timezone.now() > expiration_time

    def __str__(self):
        return f"OTP for {self.email}"
