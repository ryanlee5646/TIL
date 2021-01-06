from django.db import models

# Create your models here.


# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name = models.TextField() # 의사정보


# Doctor:Patient = 1:N
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients',)
    

# Doctor:Reservation = 1:N
# Patient:Reservation = 1:M
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


# doctor1 = Doctor.objects.create(name='Kim')
# doctor2 = Doctor.objects.create(name='Kang')
# patient1 = Patient.objects.create(name='Tom')
# patient2 = Patient.objects.create(name='John')
# Reservation.objects.create(doctor=doctor1, patient=patient2)

