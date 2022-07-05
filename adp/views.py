from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404

from .models import *
from .serializer import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Fundflow')

class CharityList(APIView):
    def get(self, request):
        charities = Charity.objects.all()
        serializer = CharitySerializer(charities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)