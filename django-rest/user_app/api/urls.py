from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import LogoutView, RegisterationView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]