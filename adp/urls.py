from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/charities/', views.CharityList.as_view()),
    path('api/charities/<int:pk>/', views.CharityDetails.as_view()),
]