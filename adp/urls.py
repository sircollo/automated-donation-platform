from django.urls import path,re_path as url
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
    path('signup/', RegisterDonorView.as_view(), name='signup'),
    path('signup-charity/', RegisterCharityView.as_view(), name='signup-charity'),
    path('signup-admin/', RegisterAdminView.as_view(), name='signup-admin'),
    path('donors/', views.donor_list),
    url(r'^donors/(?P<donor_id>\d+)/', views.donor_details),
]

# API URLS
# signin - http://127.0.0.1:8000/signin/
# signup-donor - http://127.0.0.1:8000/signup/
# signup-charity - http://127.0.0.1:8000/signup-charity/

# Donors list - http://127.0.0.1:8000/donors/
# Donor details - http://127.0.0.1:8000/donors/:id --update donor details(profile)