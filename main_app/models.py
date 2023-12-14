from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='patient')

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    emergency_contact = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    SPECIALIZATIONS = [
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('neurology', 'Neurology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('gastroenterology', 'Gastroenterology'),
        ('oncology', 'Oncology'),
        ('psychiatry', 'Psychiatry'),
        ('obgyn', 'OB/GYN'),
        ('endocrinology', 'Endocrinology'),
        ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS)
    years_of_experience = models.IntegerField()
    contact_information = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('valid', 'Valid'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_appointments')
    date_and_time = models.DateTimeField()
    purpose = models.TextField()
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.doctor.name} - {self.date_and_time.strftime('%Y-%m-%d %H:%M')}"
    
class MedicalRecords(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_medical_records') 
    date_of_record = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescriptions = models.TextField()

    def __str__(self):
        return f"Record for {self.patient.name} on {self.date_of_record.strftime('%Y-%m-%d')}"