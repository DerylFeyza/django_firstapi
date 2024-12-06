from rest_framework import serializers, exceptions
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Token
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from .utils import generate_otp
import pyotp
from .enums import TokenTypeClass, TOKEN_TYPE

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if not user.verified:
            raise exceptions.AuthenticationFailed(
                _('OTP Sent, Please Verify Your Account'), code='authentication')
        token['email'] = user.email
        token['role'] = user.role
        return token
    
class ValidateUserSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise ValidationError("Email is not registered")
        
        try:
            valid_token = Token.objects.get(user_id=user.id, token_type=TokenTypeClass.USER_VERIFICATION)
        except Token.DoesNotExist:
            raise ValidationError("Token does not exist")

        totp = pyotp.TOTP(valid_token.token_secret, interval=300)
        if not totp.verify(attrs["otp"]):
            raise ValidationError("Invalid OTP")

        valid_token.verify_user()
        valid_token.delete()
        return super().validate(attrs)
    
class SendOtpSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    purpose = serializers.ChoiceField(choices=TOKEN_TYPE, required=True)
    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise ValidationError("Email is not registered")
        
        if user.verified and attrs["purpose"] == TokenTypeClass.USER_VERIFICATION:
            raise ValidationError("User already verified")
        
        otp = generate_otp(user, token_type=attrs["purpose"])
        print(otp)
        return super().validate(attrs)

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["id","email", "password"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create_app_user(**validated_data)
        return user
        
       