from rest_framework import generics
from api.models import Patient, Drug, Overview
from api.serializers import PatientSerializer, DrugSerializer, OverviewSerializer
from collections import Counter


class PatientListByDrug(generics.ListAPIView):
    def get_queryset(self):

        # Получаем аргументы из url-строки для лекарства, если нет то список для лекарства - тест
        lekarstvo = self.request.query_params.get('medecine_product', 'Test')
        # Получаем аргументы из url-строки для посещений, если нет то дефолтное значение ноль
        visits = int(self.request.query_params.get('meet_doctor_amount', 0))

        # Получаем список всех приемов с подобным назначением
        rows = Overview.objects.filter(drug__name__contains = lekarstvo).all()
        patients = [row.patient for row in rows]

        if visits == 0:
            return patients

        else:
            final = []  # Финальный список имен для удаления из списка записей всех приемов
            a = Counter(patients) # Подсчитывам приемы для каждого пацента
            for key in a.copy(): # Удаляем имена, где меньше посещений чем надо
                if a[key] < int(visits):
                    del a[key]
            a = sorted(a, key=a.get, reverse=True)
            # Удаляем все записи для исключенных
            for key in a:
                for patient in patients:
                    if patient == key:
                        final.append(patient)

            return final

    serializer_class = PatientSerializer


class PatientByBirthDate(generics.ListAPIView):
    def get_queryset(self):
        date = self.request.query_params.get('birth_date', '2020-10-10')
        query = Patient.objects.filter(birth_date__gt = date)
        return query

    serializer_class = PatientSerializer
