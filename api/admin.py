from django.contrib import admin
from api.models import Patient, Drug, Overview


admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Overview)