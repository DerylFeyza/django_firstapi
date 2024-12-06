from django.db import models
import uuid
# import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from datetime import timezone
from .enums import USER_ROLE, TOKEN_TYPE
import pyotp

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLE, default=USER_ROLE[1][0])
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    token_secret = models.CharField(max_length=255, null=True)
    token_type = models.CharField(max_length=100, choices=TOKEN_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(auto_now_add=False, null=True)


    def __str__(self):
        return f"{str(self.user)} {self.token_secret}"

    def verify_user(self)-> None:
        self.user.verified = True
        self.user.is_active = True
        self.user.save()

   
    
    