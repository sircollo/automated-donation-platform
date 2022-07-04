from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class User(AbstractUser):
  is_charity = models.BooleanField(default=False)
  is_donor = models.BooleanField(default=False)