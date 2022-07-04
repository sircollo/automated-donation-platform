from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
# Create your views here.

def index(request):
    return HttpResponse('Welcome to Fundflow')

# Get token/login
class GetTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = GetTokenPairSerializer
    
# Register donor view
class RegisterDonorView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterDonorSerializer
    
# Register charity view 
class RegisterCharityView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterCharitySerializer
    
# Register adminview 
class RegisterAdminView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterAdminSerializer
  