from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
    path('signup/', RegisterDonorView.as_view(), name='signup'),
    path('signup-charity/', RegisterCharityView.as_view(), name='signup'),
]

# API URLS
# signin - http://127.0.0.1:8000/signin/
# signup-donor - http://127.0.0.1:8000/signup/
# signup-charity - http://127.0.0.1:8000/signup-charity/