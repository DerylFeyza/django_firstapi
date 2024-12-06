import pyotp
from datetime import datetime, timedelta, timezone
from .enums import TokenTypeClass  

def generate_otp(user, token_type: TokenTypeClass):
    from .models import Token
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
    return otp
