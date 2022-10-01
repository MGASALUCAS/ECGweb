from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

admin.site.register(Patients)
admin.site.register(patient)
admin.site.register(Post)