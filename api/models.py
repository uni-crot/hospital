from django.db import models


SEX = (
    ('мужчина','Мужчина'),
    ('женщина', 'Женщина')
)


class Patient(models.Model):
    name = models.TextField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX)
    birth_date = models.DateField()
    address = models.TextField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        # Для отображения множественного числоа
        verbose_name_plural = 'Patients'


class Drug(models.Model):
    name = models.TextField(max_length=160)
    use = models.TextField(max_length=256)
    effects = models.TextField(max_length=256)
    side_effects = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Overview(models.Model):
    priem = models.IntegerField()
    date = models.DateField()
    place = models.TextField(max_length=256)
    symptoms = models.TextField(max_length=256)
    diagnosis = models.TextField(max_length=256)
    drug = models.ForeignKey(Drug, on_delete=models.PROTECT)
    doctor = models.TextField(max_length=256)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def __str__(self):
        priem = str(self.priem)
        return priem
