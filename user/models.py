from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin

class Role(models.TextChoices):
        ADMIN = 'admin', 'admin'
        AUTHOR = 'author', 'author'

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.AUTHOR)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

# class Token(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255, null=True)
#     token_type = models.CharField(max_length=100, choices=TOKEN_TYPE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{str(self.user)} {self.token}"

#     def is_valid(self)->bool:
#         lifespan_in_seconds = float(settings.TOKEN_LIFESPAN * 60 * 60)
#         now = datetime.now(timezone.utc)
#         time_diff = now - self.created_at
#         time_diff = time_diff.total_seconds()
#         if time_diff >= lifespan_in_seconds:
#             return False
#         return True

#     def verify_user(self)-> None:
#         self.user.verified = True
#         self.user.is_active = True
#         self.user.save()

#     def generate(self) -> None:
#         if not self.token:
#             self.token = get_random_string(120)
#             self.save()

