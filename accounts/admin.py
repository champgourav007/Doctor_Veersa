from django.contrib import admin
from .models import UserModel, PatientUserModel, DoctorUserModel, Slots, SlotsTime,BookAppointment, Prescription,Reports

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PatientUserModel)
admin.site.register(DoctorUserModel)
admin.site.register(Slots)
admin.site.register(SlotsTime)
admin.site.register(BookAppointment)
admin.site.register(Prescription)
admin.site.register(Reports)