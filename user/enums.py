from dataclasses import dataclass

USER_ROLE = (
    ("admin", "admin"),
    ("author", "author"),
)

TOKEN_TYPE = (
    ('account_verification', 'account_verification'),
    ('password_reset', 'password_reset'),
)


@dataclass
class TokenTypeClass:
    USER_VERIFICATION = "account_verification"
    PASSWORD_RESET = "password_reset"
    
class UserTypeRole:
    ADMIN = "admin"
    AUTHOR = "author"
