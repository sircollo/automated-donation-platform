from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
# donor serializer dependencies
import requests
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

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
    
class DonorsView(generics.CreateAPIView):
    queryset = Donor.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonorSerializer
    

@api_view(['GET', 'POST'])
def donor_list(request):
    if request.method == 'GET':
        donors = Donor.objects.all()
        donors_serializer = DonorSerializer(donors, many=True,context={'request': request})
        return Response(donors_serializer.data)
    elif request.method == 'POST':
        donors_data = JSONParser().parse(request)
        donors_serializer = DonorSerializer(data=donors_data)
        if donors_serializer.is_valid():
            donors_serializer.save()
            return Response(donors_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(donors_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT'])
def donor_details(request, donor_id):
    try: 
        donor = Donor.objects.get(id=donor_id) 
    except Donor.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        donor_serializer = DonorSerializer(donor) 
        return Response(donor_serializer.data) 
    elif request.method == 'PUT': 
        donor_data = JSONParser().parse(request) 
        donor_serializer = DonorSerializer(donor, data=donor_data) 
        if donor_serializer.is_valid(): 
            donor_serializer.save() 
            return JsonResponse(donor_serializer.data) 
        return JsonResponse(donor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)