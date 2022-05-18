from cProfile import Profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import DoctorDobForm, DoctorForm, AppointmentType, IdForm, PatientDobForm, PatientGender
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
    # context["pk"] = pk
    # user = User.objects.get(id=pk)
    user_model = UserModel.objects.get(user_id=pk)
    if user_model.usertype == "patient":
        user_data = PatientUserModel.objects.get(patient_id=user_model.id)
        all_user = User.objects.all()

        doctors_data = []
        doctors = UserModel.objects.filter(usertype="doctor")
        print(doctors)
        for i in doctors:
            try:
                doctor_id = DoctorUserModel.objects.get(doctor_id = i.id)
                slots = Slots.objects.filter(doctor_slot_id = doctor_id)
                if slots:
                    doctors_data.append({
                        "name" : i,
                        "doctor_data" : DoctorUserModel.objects.get(doctor_id = i.id),        
                        "slots" : slots,         
                    })
            except:
                continue

        context["available_doctors"] = doctors_data



    if user_model.usertype == "doctor":
        user_data = DoctorUserModel.objects.get(doctor_id=user_model.id)
        # appointments = Appointment.objects.filter(user_id = user_data.id)
        appointments = getAllAppointments(user_data.id)
        context["appointments"] = appointments

    
    context["user"] = user_data
    context["user_model"] = user_model
    context["user_data"] = user_data
    context["pk"] = pk



    return render(request, 'accounts/home_page.html', context)

def show_profile(request, pk):
    context = {}
    user = User.objects.get(id=pk)
    user_model = UserModel.objects.get(user_id = user.id)
    if user_model.usertype == "patient":
        user_data = PatientUserModel.objects.get(patient_id = user_model.id)
        context["dob"] = PatientDobForm()
    if user_model.usertype == "doctor":
        user_data = DoctorUserModel.objects.get(doctor_id = user_model.id)
        context["dob"] = DoctorDobForm()
        

    print(user_data.street_address)
    context["user"] = user
    context["user_model"] = user_model
    context["user_data"] = user_data
    
    context["age"] = user_data.get_age()
    context["pk"] = pk
    context["idform"] = IdForm()
    context["gender"] = PatientGender()
 
    return render(request, "accounts/profile.html", context)


def change_password(password, pk):
    user = User.objects.get(id=pk)
    user.set_password(password)
    user.save()




def update_profile(request, pk):
    user_model = UserModel.objects.get(user_id=pk)
    context = {}
    print(request.POST)
    if user_model.usertype == "patient":
        user_data = PatientUserModel.objects.get(patient_id = user_model.id)
        if request.FILES.get("file"):
            file = PatientUserModel(profile_image=request.FILES.get("file"))
            file.save()
        # user_data
    if user_model.usertype == "doctor":
        if request.FILES.get("file"):
            file = DoctorUserModel(profile_image=request.FILES.get("file"))
            file.save()
        user_data = DoctorUserModel.objects.get(doctor_id = user_model.id)
    context["messages"] = "Changes is Successfully Updated!!!!"
    for key, values in request.POST.items():
        if len(values) > 0 and values != "" or values != None:
            try:
                if key == "firstname":
                    user_data.firstname = values
                if key == "lastname":
                    user_data.lastname = values
                if key == "email":
                    user_data.email = values
                if key == "dob":
                    print(values)
                    user_data.dob = values
                if key == "mobile":
                    user_data.mobile_no = values
                if key == "city":
                    user_data.city = values
                if key == "state":
                    user_data.state = values
                if key == "address":
                    user_data.street_address = values
                if key == "gender":
                    user_data.gender = values
                if key == "pincode":
                    user_data.pincode = values
                if key == "country":
                    user_data.country = values
                if key == "gov_id_type":
                    user_data.gov_id_type = values
                if key == "gov_id_number":
                    user_data.gov_id_no = values
                if key == "password":

                    if request.POST.get("password") == request.POST.get("password1"):
                        change_password(values, pk)
                    else:
                        redirect("profile", pk=pk)
                user_data.save()
            except:
                redirect("profile", pk=pk)
    
    
    return redirect("profile", pk=pk)


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




def book_appointment(request, pk, doctor, user):
    user_data = PatientUserModel.objects.get(id=user)
    slots = Slots.objects.filter(doctor_slot_id=doctor)
    available_dates = []
    today_date = datetime.date.today()
    for slot in slots[:10]:
        if slot.date >= today_date:
            available_dates.append(slot)
    # for i in available_dates:
    #     print(i)

    context = {}
    context["user"] = User.objects.get(id=pk)
    context["user_model"] = UserModel.objects.get(user_id=pk)
    context["clicked_date"] = available_dates[0]
    context["user_data"] = user_data

    if request.method == "POST":
        print(request.POST)
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

    if len(available_dates) == 0:
        context["errors"] = "Not available"

    context["available_dates"] = available_dates
    context["appointment_type"] = AppointmentType()
    context["doctor"] = doctor
    context["pk"] = pk

    return render(request, "accounts/book_appointment.html", context)

def save_appointment(request, pk, doctor, user):
    data  = request.POST
    full_name = PatientUserModel.objects.get(id=user).__str__()
    appointment_type = data.get("appointment_type")
    slots = data.get("time")
    print(data)

    appointment = Appointment.objects.create(user_id=pk,full_name=full_name, appointment_type=appointment_type)
    appointment.slots = str(slots)
    appointment.save()

    book_appointment = BookAppointment.objects.create(doctor_id=doctor, appointment_id=appointment.id, full_name=full_name, appointment_type=appointment_type)
    book_appointment.save()

    prescription = Prescription.objects.create(appointment_id=book_appointment.id)
    prescription.save()
    reports = Reports.objects.create(prescription_id=prescription.id)
    reports.save()

    return render(request, "accounts/done.html")



def set_slots(request, pk):
    context = {}
    user = User.objects.get(id=pk)
    user_model = UserModel.objects.get(user_id=pk)
    user_data = DoctorUserModel.objects.get(doctor_id=user_model.id)

    if request.method == "POST":
        data = request.POST
        print(data)
        slotdate = Slots.objects.create(doctor_slot_id = user_data.id, date=data.get("date"))
        slottime = SlotsTime.objects.create(slottiming_id=slotdate.id, time=data.get("time"))
        slottime.save()
        slotdate.save()
        
    # available_dates = 
    context["date"] = datetime.date.today()
    context["user"] = user
    context["user_model"] = user_model
    context["user_data"] = user_data
    context["pk"] = pk

    return render(request, "accounts/book_appointment.html", context)
