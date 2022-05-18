from django.forms import ModelForm
from .models import Appointment, DoctorUserModel, PatientUserModel, UserModel



class DoctorForm(ModelForm):
    class Meta:
        model = DoctorUserModel
        # exclude = ("user", "unique_id")
        fields = ("specialist", )

class AppointmentType(ModelForm):
    class Meta:
        model = Appointment
        fields = ("appointment_type",)

class IdForm(ModelForm):
    class Meta:
        model = PatientUserModel
        fields = ("gov_id_type",)

class PatientGender(ModelForm):
    class Meta:
        model = UserModel
        fields = ("gender",)

class PatientDobForm(ModelForm):
    class Meta:
        model = PatientUserModel
        fields = ("dob",)

class DoctorDobForm(ModelForm):
    class Meta:
        model = DoctorUserModel
        fields = ("dob",)