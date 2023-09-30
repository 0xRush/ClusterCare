from django.contrib import admin

# Register your models here.
from .models import Mobileclinic, Resources, Activity, Patient, User

admin.site.register(User)
admin.site.register(Mobileclinic)
admin.site.register(Resources)
admin.site.register(Activity)
admin.site.register(Patient)
