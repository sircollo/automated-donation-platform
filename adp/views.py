from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Fundflow')

