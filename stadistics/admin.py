from django.contrib import admin
from .models import Watersample, Modelprofile

myModels = [Watersample, Modelprofile]

# Register your models here.
admin.site.register(myModels)