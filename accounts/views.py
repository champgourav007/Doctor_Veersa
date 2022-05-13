from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from .models import UserModel, PatientUserModel
from django.contrib.auth.models import User

# Create your views here.
def test(request):
    return HttpResponse("Hello!!!!!! Test Done")


def loginView(request):
    if request.method == "POST":
        data = request.POST
        usertype = data.get("usertype")
        username = data.get("username")
        first_name = data.get("firstname")
        middle_name = data.get("middlename")
        lastname = data.get("lastname")
        mobileNo = data.get("mobileno")
        gender = data.get("gender")
        password = data.get("password")
        password1 = data.get("password1")
        if password == password1:
            user = User.objects.create_user(username=username, password=password)
            if usertype == "Patient":
                patient = UserModel.objects.create(user_id=user.id, first_name=first_name, gender=gender)
                patient_user = PatientUserModel.objects.create(patient_id=patient.id)
        else:
            errors = []
            return render(request, "accounts/login.html", {
                "errors": errors,
            })
        return render(request, "accounts/done.html")
    return render(request, "accounts/login.html")