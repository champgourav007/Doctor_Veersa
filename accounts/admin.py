from django.contrib import admin
from .models import UserModel, PatientUserModel, DoctorUserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PatientUserModel)
admin.site.register(DoctorUserModel)