from django.contrib import admin
from .models import Charity, Donor, Donations

# Register your models here.

admin.site.register(Charity)
admin.site.register(Donor)
admin.site.register(Donations)
