from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import LogoutView, RegisterationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]