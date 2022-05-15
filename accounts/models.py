from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from Doctor_Veersa import settings

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(null=True)
    GENDER_CHOICES = (
        ("Male","M"),
        ("Female","F"),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")

    USER_TYPE = (
        ('Patient','Patient'),
        ('Doctor', 'Doctor')
    )

    usertype = models.CharField(max_length=100, choices=USER_TYPE, default='Patient', null=True)

    def __str__(self):
        return f"{self.user.first_name}"

class PatientUserModel(models.Model):
    patient = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    street_address = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="media/patientImages", default="media/default.png", null=True, blank=True)

    def __str__(self):
        return f"{self.patient.first_name}"

       
SPECIALIST_CHOICES = (
        ("Sports Medicine Specialists","Sports Medicine Specialists"),
        ("General Surgeons", "General Surgeons"),
        ("Allergists/ Immunologists","Allergists/Immunologists"),
        ("Anesthesiologists","Anesthesiologists"),
        ("Cardiologists","Cardiologists"),
        ("Colon and Rectal Surgeons", "Colon and Rectal Surgeons"),
        ("Critical Care Medicine Specialists", "Critical Care Medicine Specialists"),
        ("Dermatologists", "Dermatologists"),
        ("Endocrinologists", "Endocrinologists"),
        ("Urologists", "Urologists"),
        ("Rheumatologists", "Rheumatologists"),
        ("Radiologists", "Radiologists"),
        ("Pulmonologists", "Pulmonologists"),
        ("Psychiatrists", "Psychiatrists"),
        ("Preventive Medicine Specialists", "Preventive Medicine Specialists"),
        ("Podiatrists", "Podiatrists"),
        ("Plastic Surgeons", "Plastic Surgeons"),
        ("Physiatrists", "Physiatrists"),
        ("Pediatricians", "Pediatricians"),
        ("Pathologists","Pathologists"),
        ("Otolaryngologists", "Otolaryngologists"),
        ("Osteopaths", "Osteopaths"),
        ("Ophthalmologists", "Ophthalmologists"),
        ("Oncologists", "Oncologists"),
        ("Obstetricians and Gynecologists", "Obstetricians and Gynecologists"),
        ("Neurologists", "Neurologists"),
        ("Nephrologists", "Nephrologists"),
        ("Medical Geneticists", "Medical Geneticists"),
        ("Emergency Medicine Specialists", "Emergency Medicine Specialists"),
        ("Others", "Others"),

    )

class DoctorUserModel(models.Model):
    doctor = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    clinic_address = models.TextField()
    profile_image = models.ImageField(upload_to="media/doctorImages", default= "media/default.png", null=True, blank=True)
    doctor_certificate = models.ImageField(upload_to="media/doctorImages", null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    

    specialist = models.CharField(max_length=255, choices=SPECIALIST_CHOICES, default="Sports Medicine Specialists")

    








