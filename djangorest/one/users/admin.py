from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(doctors)
admin.site.register(appointments)
admin.site.register(profile)