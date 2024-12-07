import pyotp
from datetime import datetime, timedelta, timezone
from .enums import TokenTypeClass
from typing import Dict, Any
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(subject: str, recipient_list: list, html_alternative: Any, attachment: Dict = None):
    msg = EmailMultiAlternatives(
        subject, '', settings.EMAIL_HOST_USER, recipient_list
    )
    if attachment is not None:
        msg.attach(
            attachment.get('name'), attachment.get('file'), attachment.get('type')
        )
    msg.attach_alternative(html_alternative, "text/html")
    msg.send(fail_silently=False)

def generate_otp(user, token_type: TokenTypeClass):
    from .models import Token
    from .tasks import send_user_creation_email
    totp = pyotp.TOTP(pyotp.random_base32(), interval=300)
    otp = totp.now()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=5)
    Token.objects.update_or_create(
        user=user,
        defaults={
            'token_secret': totp.secret,
            'token_type': token_type,
            'expires_at': expires_at,
            'created_at': datetime.now(timezone.utc)
        }
    )
    user_data = {
        "email": user.email,
        "token": otp
    }  
    send_user_creation_email(user_data)

