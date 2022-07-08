from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from .models import *



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_donor:
            Donor.objects.create(user=instance)
        elif instance.is_charity:
            Charity.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_donor:
        instance.donor.save()
    elif instance.is_charity:
        instance.charity.save()