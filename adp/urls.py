from django.urls import path,re_path as url
from . import views
from .views import *


from rest_framework_jwt.views import (obtain_jwt_token,
                                        verify_jwt_token,
                                        refresh_jwt_token)

urlpatterns = [
    path('', views.index, name='index'),



    #Users API endpoints
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    
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
    url(r'api/charity/(?P<charity_id>\d+)/donations/$', views.CharitiesDonationsList),
    url(r'api/charity/(?P<charity_id>\d+)/donations/(?P<donation_id>\d+)/$', views.CharitiesDonationsdetails),   

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
    
    url(r'charity/(?P<charity_id>\d+)/beneficiaries/$', views.charitybeneficiaries_list),
    url(r'charity/(?P<charity_id>\d+)/beneficiary/(?P<beneficiary_id>\d+)/$', views.charitybeneficiary_details),
    
    # all anonymous donations view
    url(r'api/anon/$', views.anonnymous_donation),
    # charity's anonymous donations
    url(r'api/charity/(?P<charity_id>\d+)/anon_donations/$', views.anonnymous_donation_list),
    
    url(r'^login', views.LoginUser.as_view()),
    url(r'^token_auth', obtain_jwt_token),
    url(r'^token_refresh', refresh_jwt_token),
    url(r'^token_verify', verify_jwt_token),
    # url(r'^register', views.CreateUser.as_view()),
    
    # url(r'^user',views.GetUser),


]

# API URLS
# signin - http://127.0.0.1:8000/signin/
# signup-donor - http://127.0.0.1:8000/signup/
# signup-charity - http://127.0.0.1:8000/signup-charity/
# signup-admin - http://127.0.0.1:8000/signup-admin/

# all users


# Donors
# Donors list - http://127.0.0.1:8000/donors/
# Single Donor details - http://127.0.0.1:8000/donors/:id --update donor details(profile)

# Beneficiaries - subject to correction
# Beneficiaries list - http://127.0.0.1:8000/charity/beneficiaries/
# Single Beneficiary details - http://127.0.0.1:8000/charity/beneficiaries/:id --update/delete beneficiary details(profile)

# this (below) endpoints should be used - confirmed working
# each charity beneficiary list - http://127.0.0.1:8000/charity/charity_id/beneficiaries/ - Get,put,post,delete
# individual beneficiary to a charity - http://127.0.0.1:8000/charity/charity_id/beneficiary/beneficiary_id - Get,put,post,delete


# Administrator - endpoints
# all charities - http://127.0.0.1:8000/api/charities/ - receive application
# each charity  - http://127.0.0.1:8000/api/charities/<int:pk>/ 'Approve', 'Delete',

# post donations
#  http://127.0.0.1:8000/api/donations/