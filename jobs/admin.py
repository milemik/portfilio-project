from django.contrib import admin

# Register your models here.
# ubacujemo clasu Job iz models.py fajla
from .models import Job

admin.site.register(Job)
