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

class FeedbackDetails(APIView):
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    #To get a particular feedback
    def get(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    #To update a particular feedback
    def put(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular feedback
    def delete(self, request, pk, format=None):
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationsList(APIView):
    def get(self, request):
        donations = Donations.objects.all()
        serializer = DonationsSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonationsDetails(APIView):
    def get_object(self, pk):
        try:
            return Donations.objects.get(pk=pk)
        except Donations.DoesNotExist:
            raise Http404

    #To get a particular donation
    def get(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationsSerializer(donation)
        return Response(serializer.data)

    #To update a particular donation
    def put(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationsSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular donation
    def delete(self, request, pk, format=None):
        donation = self.get_object(pk)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostsList(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDetails(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    #To get a particular post
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    #To update a particular post
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular post
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)