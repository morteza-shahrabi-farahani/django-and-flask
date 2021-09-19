from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
from api.models import Link
from api.serializer import LinkSerializer


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer

class Redirector(View):
    def get(self,request,shortener_link, *args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=Link.objects.filter(shorten_link=shortener_link).first().original_link
        return redirect(redirect_link)
