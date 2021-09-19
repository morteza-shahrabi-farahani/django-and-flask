from django.urls import path

from api.views import ShortenerListAPIView, ShortenerCreateAPIView

app_name = 'api'

urlpatterns = [
    path('', ShortenerListAPIView.as_view(), name='all_linkss'),
    path('create/', ShortenerCreateAPIView.as_view(), name='create-api'),
]