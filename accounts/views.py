from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import DoctorForm
from .models import DoctorUserModel, UserModel, PatientUserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index_view(request):
    doctors = UserModel.objects.filter(usertype = 'doctor')
    d = []
    for i in doctors:
        if len(d) == 10:
            break
        print(d.append({
            "doctor":User.objects.get(id=i.user_id), 
            "specialist":DoctorUserModel.objects.get(doctor_id=i.id).specialist,
            "image" : DoctorUserModel.objects.get(doctor_id=i.id).profile_image,
        }))
    return render(request, "accounts/index.html",{
        "doctors" : d,
    })


def signup_view(request):
    if request.method == "POST":
        data = request.POST
        usertype = data.get("usertype")
        username = data.get("username")
        first_name = data.get("firstname")
        middle_name = data.get("middlename")
        last_name = data.get("lastname")
        mobileNo = data.get("mobileNo")
        gender = data.get("gender")
        password = data.get("password")
        password1 = data.get("password1")
        email = data.get("email")
        if password == password1:
            try:
                user = User.objects.create_user(username=username, password=password)
            except:
                return render(request, "accounts/signup.html",{
                    "messages" : "Account Already Exists!!! Please Login!!!"
                })
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            print(usertype)
            if usertype == "patient":
                patient = UserModel.objects.create(user_id=user.id, gender=gender, usertype=usertype, mobile_no=mobileNo)
                patient_user = PatientUserModel.objects.create(patient_id=patient.id)

            if usertype == "doctor":
                doctor = UserModel.objects.create(user_id=user.id, gender=gender, usertype=usertype)
                doctor_user = DoctorUserModel.objects.create(doctor_id=doctor.id)
        else:
            return render(request, "accounts/signup.html", {
                "message": "Password Does't Match",
            })
        return redirect('login-page')
    return render(request, "accounts/signup.html",{
        "specialists" : DoctorForm(),
    })

def login_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        usertype = data.get("usertype")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            login_user = UserModel.objects.get(user_id = user.id)
            if usertype == "patient":
                try:
                    print(login_user.id)
                    user_data = PatientUserModel.objects.get(patient_id = login_user.id)
                    print(user_data.id)
                except:
                    messages.error(request, "You are not a Patient!!!!!\n Please Sign Up")
                    return redirect('login-page')

            if usertype == "doctor":
                try:
                    print(login_user.id)
                    user_data = DoctorUserModel.objects.get(doctor_id = login_user.id)
                    print(user_data.id)
                except:
                    messages.error(request, "You are not a Doctor!!!!!\n Please Sign Up")
                    return redirect('login-page')

            return render(request, "accounts/home_page.html",{
                    "user" : {
                        "username" : username,
                        "usertype" : usertype,
                    },
                    "user_data" : user_data,
                    "login_user" : login_user,
                })

            # if usertype == "patient":
            #     return render(request, "accounts/home_page.html",{
            #         "user" : {username}
            #     })
        else:
            return render(request, 'accounts/login.html', {
                "messages" : "Account not Found!!!! Please Sign Up!!",
            })


    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return render(request, "accounts/done.html")


def book_appointment():
    pass