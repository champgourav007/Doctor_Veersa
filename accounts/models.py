from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=250, unique=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.IntegerField(null=True)
    email = models.EmailField(unique=True, null=True)
    GENDER_CHOICES = (
        ("Male","M"),
        ("Female","F"),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")

    def __str__(self):
        return f"{self.first_name}"

class PatientUserModel(models.Model):
    patient = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    street_address = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="media/patientImages", null=True, blank=True)

    def __str__(self):
        return f"{self.patient.first_name}"

class DoctorUserModel(models.Model):
    doctor = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    clinic_address = models.TextField()
    profile_image = models.ImageField(upload_to="media/doctorImages", null=True, blank=True)
    doctor_certificate = models.ImageField(upload_to="media/doctorImages", null=True, blank=True)
    about = models.TextField(null=True, blank=True)
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

    specialist = models.CharField(max_length=255, choices=SPECIALIST_CHOICES, default="Sports Medicine Specialists")

    







