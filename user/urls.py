from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns= [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify", views.VerifyAccountView.as_view(), name="verify"),
    path("getotp", views.GetOtpView.as_view(), name="get_otp"),
    path('token', views.CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
