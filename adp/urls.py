from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #charities API endpoints
    path('api/charities/', views.CharityList.as_view()),
    path('api/charities/<int:pk>/', views.CharityDetails.as_view()),

    #donations API endpoints
    path('api/donations/', views.DonationsList.as_view()),
    path('api/donations/<int:pk>/', views.DonationsDetails.as_view()),

    #feedback API endpoints
    path('api/feedback/', views.FeedbackList.as_view()),
    path('api/feedback/<int:pk>/', views.FeedbackDetails.as_view()),

    #posts API endpoints
    path('api/posts/', views.PostsList.as_view()),
    path('api/posts/<int:pk>/', views.PostsDetails.as_view()),
]