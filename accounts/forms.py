from django.forms import ModelForm
from .models import Appointment, DoctorUserModel

class DoctorForm(ModelForm):
    class Meta:
        model = DoctorUserModel
        # exclude = ("user", "unique_id")
        fields = ("specialist", )

class AppointmentType(ModelForm):
    class Meta:
        model = Appointment
        fields = ("appointment_type",)