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

    #apply as a charity
    def post(self, request, format=None):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CharityDetails(APIView):
    def get_object(self, pk):
        try:
            return Charity.objects.get(pk=pk)
        except Charity.DoesNotExist:
            raise Http404

    #To get a particular charity
    def get(self, request, pk, format=None):
        charity = self.get_object(pk)
        serializer = CharitySerializer(charity)
        return Response(serializer.data)

    #To update a particular charity
    def put(self, request, pk, format=None):
        charity = self.get_object(pk)
        serializer = CharitySerializer(charity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular charity
    def delete(self, request, pk, format=None):
        charity = self.get_object(pk)
        charity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class FeedbackList(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

