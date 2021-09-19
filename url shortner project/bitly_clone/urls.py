from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from api.views import Redirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls',namespace='api')),
    path('<str:shortener_link>/', Redirector.as_view(), name='redirector')
]
