from django.urls import path
from api.views import PatientListByDrug, PatientByBirthDate

urlpatterns = [
    path('patient_list_by_drug', PatientListByDrug.as_view()),
    path('patien_by_birth_date', PatientByBirthDate.as_view())
]