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
    
# donor list
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

# single donor view   
@api_view(['GET', 'PUT'])
def donor_details(request, donor_id):
    try: 
        donor = Donor.objects.get(id=donor_id) 
    except Donor.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)  
    if request.method == 'GET': 
        donor_serializer = DonorSerializer(donor,many=True) 
        return Response(donor_serializer.data) 
    elif request.method == 'PUT': 
        donor_data = JSONParser().parse(request) 
        donor_serializer = DonorSerializer(donor, data=donor_data) 
        if donor_serializer.is_valid(): 
            donor_serializer.save() 
            return JsonResponse(donor_serializer.data) 
        return JsonResponse(donor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#beneficiaries list 
@api_view(['GET','DELETE','POST'])
def beneficiaries_list(request):
    if request.method == 'GET':
        beneficiaries = Beneficiary.objects.all()
        beneficiaries_serializer = BeneficiariesSerializer(beneficiaries, many=True,context={'request': request})
        return Response(beneficiaries_serializer.data)
    elif request.method == 'POST':
        beneficiaries_data = JSONParser().parse(request)
        beneficiaries_serializer = BeneficiariesSerializer(data=beneficiaries_data)
        if beneficiaries_serializer.is_valid():
            beneficiaries_serializer.save()
            return Response(beneficiaries_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(beneficiaries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Beneficiary.objects.all().delete()
        return JsonResponse({'message': '{} All Beneficiaries successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
# single beneficiary view   
@api_view(['GET', 'PUT','DELETE','POST'])
def beneficiary_details(request, beneficiary_id):
    try: 
        beneficiary = Beneficiary.objects.get(id=beneficiary_id) 
    except Beneficiary.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary,many=True) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'PUT': 
        beneficiary_data = JSONParser().parse(request) 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, data=beneficiary_data) 
        if beneficiary_serializer.is_valid(): 
            beneficiary_serializer.save() 
            return JsonResponse(beneficiary_serializer.data) 
        return JsonResponse(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        # return redirect('http://127.0.0.1:8000/beneficiaries/')
        return JsonResponse({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# each charity beneficiary list  
@api_view(['GET', 'PUT','DELETE','POST'])
def charitybeneficiaries_list(request, charity_id):
    try:
        charities = Charity.objects.get(id=charity_id)
        beneficiary = Beneficiary.objects.filter(charity=charities)
    except Beneficiary.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, many=True) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'POST':
        beneficiary_serializer = BeneficiariesSerializer(data=request.POST)
        if beneficiary_serializer.is_valid():
            beneficiary_serializer.save(charity_id=charity_id)
            return Response(beneficiary_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        return JsonResponse({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# single charity beneficiary view   
@api_view(['GET', 'PUT','DELETE','POST'])
def charitybeneficiary_details(request, charity_id, beneficiary_id):
    try: 
        beneficiary = Beneficiary.objects.get(id=beneficiary_id)
        charities = Charity.objects.get(id=charity_id) 
    except Beneficiary.DoesNotExist: 
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'PUT': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, data=request.data) 
        if beneficiary_serializer.is_valid(): 
            beneficiary_serializer.save() 
            return Response(beneficiary_serializer.data) 
        return Response(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        return Response({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)