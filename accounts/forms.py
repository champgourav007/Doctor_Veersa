from django.forms import ModelForm
from .models import DoctorUserModel

class DoctorForm(ModelForm):
    class Meta:
        model = DoctorUserModel
        # exclude = ("user", "unique_id")
        fields = ("specialist", )