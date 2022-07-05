from django.urls import path,re_path as url
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),


    #charities API endpoints
    path('api/charities/', views.CharityList.as_view()),
    path('api/charities/<int:pk>/', views.CharityDetails.as_view()),

    #donors API endpoints
    path('api/donors/', views.DonorList.as_view()),
    path('api/donors/<int:pk>/', views.DonorDetails.as_view()),

    #donations API endpoints
    path('api/donations/', views.DonationsList.as_view()),
    path('api/donations/<int:pk>/', views.DonationsDetails.as_view()),

    #feedback API endpoints
    path('api/feedback/', views.FeedbackList.as_view()),
    path('api/feedback/<int:pk>/', views.FeedbackDetails.as_view()),

    #posts API endpoints
    path('api/posts/', views.PostsList.as_view()),
    path('api/posts/<int:pk>/', views.PostsDetails.as_view()),

    #Charity Donations API endpoints
    path('api/charities/<int:pk>/donations/', views.CharityDonationsList.as_view()),    

    path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
    path('signup/', RegisterDonorView.as_view(), name='signup'),
    path('signup-charity/', RegisterCharityView.as_view(), name='signup-charity'),
    path('signup-admin/', RegisterAdminView.as_view(), name='signup-admin'),
    # donor endpoints
    path('donors/', views.donor_list),
    url(r'^donors/(?P<donor_id>\d+)/', views.donor_details),
    # beneficiaries endpoints
    path('charity/beneficiaries/', views.beneficiaries_list),
    url(r'^charity/beneficiaries/(?P<beneficiary_id>\d+)/', views.beneficiary_details),
    
    url(r'charity/(?P<charity_id>\d+)/beneficiaries/', views.charitybeneficiaries_list),
    url(r'charity/(?P<charity_id>\d+)/beneficiary/(?P<beneficiary_id>\d+)/', views.charitybeneficiary_details),
    
]

# API URLS
# signin - http://127.0.0.1:8000/signin/
# signup-donor - http://127.0.0.1:8000/signup/
# signup-charity - http://127.0.0.1:8000/signup-charity/

# Donors
# Donors list - http://127.0.0.1:8000/donors/
# Single Donor details - http://127.0.0.1:8000/donors/:id --update donor details(profile)

# Beneficiaries - subject to correction
# Beneficiaries list - http://127.0.0.1:8000/charity/beneficiaries/
# Single Beneficiary details - http://127.0.0.1:8000/charity/beneficiaries/:id --update/delete beneficiary details(profile)

# this (below) endpoints should be used
# each charity beneficiary list - http://127.0.0.1:8000/charity/charity_id/beneficiaries/ - Get,put,post,delete
# individual beneficiary to a charity - http://127.0.0.1:8000/charity/charity_id/beneficiary/beneficiary_id - Get,put,post,delete

