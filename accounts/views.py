from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import DoctorForm, AppointmentType
from .models import BookAppointment, DoctorUserModel, Prescription, Reports, UserModel, PatientUserModel, Slots, SlotsTime, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
# Create your views here.

def getAllAppointments(id):
    all_appointments = BookAppointment.objects.filter(doctor_id=id)
    print(all_appointments)
    return all_appointments

def home_page(request, pk):
    context = {}
    # user = User.objects.get(id=pk)
    user_model = UserModel.objects.get(user_id=pk)
    if user_model.usertype == "patient":
        # user = PatientUserModel.objects.get(patient_id=user_model.id)
        user_data = PatientUserModel.objects.get(patient_id=user_model.id)
        all_user = User.objects.all()

        doctors_data = []
        doctors = UserModel.objects.filter(usertype="doctor")
        for i in doctors:
            doctors_data.append({
                "name" : i,
                "doctor_data" : DoctorUserModel.objects.get(doctor_id = i.id)                 
            })

        context["available_doctors"] = doctors_data



    if user_model.usertype == "doctor":
        user_data = DoctorUserModel.objects.get(doctor_id=user_model.id)
        # appointments = Appointment.objects.filter(user_id = user_data.id)
        appointments = getAllAppointments(user_data.id)
        context["appointments"] = appointments

    
    context["user"] = user_data
    context["user_model"] = user_model
    context["user_data"] = user_data



    return render(request, 'accounts/home_page.html', context)

def show_profile(request, pk):
    pass

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
            "slot" : DoctorUserModel.objects.get(doctor_id=i.id).id,
        }))
    return render(request, "accounts/index.html",{
        "doctors" : d
    })


def signup_view(request):
    if request.method == "POST":
        data = request.POST
        usertype = data.get("usertype")
        print(usertype)
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
                    "message" : "Account Already Exists!!! Please Login!!!",
                    "specialists" : DoctorForm(),
                })
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            if usertype == "patient":
                patient = UserModel.objects.create(user_id=user.id, gender=gender, usertype=usertype, mobile_no=mobileNo)
                patient_user = PatientUserModel.objects.create(patient_id=patient.id)

            if usertype == "doctor":
                specialist = data.get("specialist")
                doctor = UserModel.objects.create(user_id=user.id, gender=gender, usertype=usertype, mobile_no=mobileNo)
                doctor_user = DoctorUserModel.objects.create(doctor_id=doctor.id, specialist=specialist)
        else:
            return render(request, "accounts/signup.html", {
                "message": "Password Doesn't Match",
                "specialists" : DoctorForm(),
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
                    user_data = PatientUserModel.objects.get(patient_id = login_user.id)
                except:
                    return render(request,'accounts/login.html', {
                        "messsages" : "Account not Found!!!!",
                    })

            if usertype == "doctor":
                try:
                    
                    user_data = DoctorUserModel.objects.get(doctor_id = login_user.id)
                    
                except:
                    
                    return render(request,'accounts/login.html', {
                        "messages" : "Account not Found!!!!",
                    })

            context = {
                "user" : user,
                "user_details" : {
                    "user_common_details" : login_user,
                    "user_data" : user_data,
                }
            }

            # return render(request, "accounts/home_page.html", context)
            return redirect('home-page', pk=user.id)
        else:
            return render(request, 'accounts/login.html', {
                "messages" : "Account not Found!!!! Please Sign Up!!",
            })


    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('index-page')




def book_appointment(request, pk, user):
    user_data = PatientUserModel.objects.get(id=user)
    slots = Slots.objects.filter(doctor_slot_id=pk)
    available_dates = []
    today_date = datetime.date.today()
    for slot in slots[:10]:
        if slot.date >= today_date:
            available_dates.append(slot)
    # for i in available_dates:
    #     print(i)

    context = {}
    context["user"] = user_data
    context["clicked_date"] = available_dates[0]

    if request.method == "POST":
        date = request.POST.get("date")
        available_timings = None
        for slot in slots:
            # print(slot.date)
            if str(date) == str(slot.date):
                available_timings = SlotsTime.objects.filter(slottiming_id=slot.id)

        if available_timings:
            context["available_timings"] = available_timings
        # print(context )
        context["clicked_date"] = str(date)
        # context["user"] = 
        # return render(request, "accounts/book_appointment.html", context)
        
    # available_timings = []
    # for slot in available_dates:
    #     available_timings.append(SlotsTime.objects.filter(slottiming_id=slot.id))
    # for i in available_timings:
    #     print(i)

    if len(available_dates) == 0:
        # print("helli")
        context["errors"] = "Not available"

    context["available_dates"] = available_dates
    context["appointment_type"] = AppointmentType()
    context["doctor"] = pk
    # print(context)
    return render(request, "accounts/book_appointment.html", context)

def save_appointment(request, doctor, user):
    data  = request.POST
    print(data)
    full_name = PatientUserModel.objects.get(id=user).__str__()
    appointment_type = data.get("appointment_type")
    slots = data.get("time")
    appointment = Appointment.objects.create(user_id=user,full_name=full_name, appointment_type=appointment_type)
    appointment.slots = slots
    appointment.save()

    book_appointment = BookAppointment.objects.create(doctor_id=doctor, appointment_id=appointment.id, full_name=full_name, appointment_type=appointment_type)
    book_appointment.save()

    prescription = Prescription.objects.create(appointment_id=book_appointment.id)
    prescription.save()
    reports = Reports.objects.create(prescription_id=prescription.id)
    reports.save()

    return HttpResponse("dome")


