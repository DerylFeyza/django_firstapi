from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from .enums import TokenTypeClass

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("verified", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)
    
    def create_app_user(self, email, **extra_fields):
        from .utils import generate_otp
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.save()
        otp = generate_otp(user, token_type=TokenTypeClass.USER_VERIFICATION)
        print(otp)
        return user