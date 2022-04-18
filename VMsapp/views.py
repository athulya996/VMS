from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from VMsapp.form import Hospitalform, Complaintform, Vaccineform, LoginRegister, Nurse_register, Userform
from VMsapp.models import Nurse, User, Hospital, Complaint, Appointment, Vaccine, Report


def main_home(request):
    return render(request, 'main_home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            if user.is_nurse:
                return redirect('nurse_home')
            if user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'login_page.html')


def admin_home(request):
    return render(request, 'admin_home.html')


@login_required(login_url='login_view')
def view_nurse(request):
    nurse = Nurse.objects.all()
    return render(request, 'admintemp/view_nurse.html', {'nurse': nurse})


@login_required(login_url='login_view')
def nurse_delete(request, user_id):
    n = Nurse.objects.get(user_id=user_id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Nurse Deleted Successfully")
        return redirect('view_nurse')
    # else:
    #     return redirect('view_nurse')


@login_required(login_url='login_view')
def user(request):
    user = User.objects.all()
    return render(request, 'admintemp/view_user.html', {'user': user})


@login_required(login_url='login_view')
def user_delete(request, id):
    n = User.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "User Deleted Successfully")
        return redirect('view_user')
    else:
        return redirect('view_user')


@login_required(login_url='login_view')
def hospital_add(request):
    form = Hospitalform()
    if request.method == 'POST':
        form = Hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Hospital Added Successfully")
            return redirect('view_hospital')
    return render(request, 'admintemp/add_hospital.html', {'form': form})


@login_required(login_url='login_view')
def hospital(request):
    hospital = Hospital.objects.all()
    return render(request, 'admintemp/view_hospital.html', {'hospital': hospital})


@login_required(login_url='login_view')
def update_hospital(request, id):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        form = Hospitalform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Hospital Updated Successfully")
            return redirect('view_hospital')
    else:
        form = Hospitalform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_hospital.html', {'form': form})


@login_required(login_url='login_view')
def hospital_delete(request, id):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Hospital Deleted Successfully")
        return redirect('view_hospital')
    else:
        return redirect('view_hospital')


@login_required(login_url='login_view')
def complaint_view(request):
    comp = Complaint.objects.all()
    return render(request, 'admintemp/complaint_view.html', {'comp': comp})


@login_required(login_url='login_view')
def complaint_reply(request, id):
    n = Complaint.objects.get(id=id)
    if request.method == 'POST':
        form = Complaintform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Student Updated Successfully")
            return redirect('complaint_view')
    else:
        form = Complaintform(request.POST or None, instance=n)
    return render(request, 'admintemp/comp_reply.html', {'form': form})


@login_required(login_url='login_view')
def Approving_apnmt(request):
    appoin = Appointment.objects.all()
    return render(request, 'admintemp/appointment_shedule.html', {'appoin': appoin})


@login_required(login_url='login_view')
def approve_appoint(request,id):
    n=Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    return redirect('appointment_shedule')


@login_required(login_url='login_view')
def reject_appoint(request, id):
    n = Appointment.objects.get(id=id)
    n.delete()
    return redirect('appointment_shedule')


@login_required(login_url='login_view')
def vaccine_approve(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.vaccinated = True
    appoint.save()
    return redirect('view_appointment')


@login_required(login_url='login_view')
def appointment_view(request):
    appointment = Appointment.objects.all()
    return render(request, 'admintemp/view_appointment.html', {'appointment': appointment})


@login_required(login_url='login_view')
def vaccine_add(request):
    if request.method == 'POST':
        form = Vaccineform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Vaccine Added Successfully")
            return redirect('view_vaccine')
    else:
        form = Vaccineform()
    return render(request, 'admintemp/add_vaccine.html', {'form': form})


@login_required(login_url='login_view')
def view_vaccine(request):
    vaccine = Vaccine.objects.all()
    return render(request, 'admintemp/view_vaccine.html', {'vaccine': vaccine})


@login_required(login_url='login_view')
def vaccine_update(request, id):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = Vaccineform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Vaccine Updated Successfully")
            return redirect('view_vaccine')
    else:
        form = Vaccineform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_vaccine.html', {'form': form})


@login_required(login_url='login_view')
def vaccine_delete(request, id):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Vaccine Deleted Successfully")
        return redirect('view_vaccine')
    else:
        return redirect('view_vaccine')


@login_required(login_url='login_view')
def view_report(request):
    report = Report.objects.all()
    return render(request, 'admintemp/view_report.html', {'report': report})


@login_required(login_url='login_view')
def nurse_register(request):
    login_form = LoginRegister()
    nurse_form = Nurse_register()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        nurse_form = Nurse_register(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            user = login_form.save(commit=False)
            user.is_nurse = True
            user.save()
            nurse = nurse_form.save(commit=False)
            nurse.user = user
            nurse.save()
            messages.info(request, "Nurse Registered Successfully")
            return redirect('login_page')
    return render(request, 'nursereg_form.html', {'login_form': login_form, 'nurse_form': nurse_form})


@login_required(login_url='login_view')
def user_register(request):
    login_form = LoginRegister()
    user_form = Userform()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = Userform(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, "User Registered Successfully")
            return redirect('login_page')
    return render(request, 'userreg_form.html', {'login_form': login_form, 'user_form': user_form})


@login_required(login_url='login_view')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login_view')
