from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from VMsapp.filter import VaccineFilter, UserFilter, HospitalFilter
from VMsapp.form import Complaintnurse, Reportform
from VMsapp.models import Vaccine, User, Hospital, Complaint, Appointment, Report


def nurse_home(request):
    return render(request, 'nursetemp/nurse_home.html')


@login_required(login_url='login_view')
def view_vaccine(request):
    v = Vaccine.objects.all()
    vaccineFilter = VaccineFilter(request.GET, queryset=v)
    v = vaccineFilter.qs
    context = {
        'vaccine': v,
        'vaccineFilter': vaccineFilter,
    }
    return render(request, 'nursetemp/nview_vaccine.html', context)


@login_required(login_url='login_view')
def view_user(request):
    v = User.objects.all()
    userFilter = UserFilter(request.GET, queryset=v)
    v = userFilter.qs
    context = {
        'user': v,
        'userFilter': userFilter,
    }
    return render(request, 'nursetemp/nview_user.html', context)


@login_required(login_url='login_view')
def view_hospital(request):
    v = Hospital.objects.all()
    hospitalFilter = HospitalFilter(request.GET, queryset=v)
    v = hospitalFilter.qs
    context = {
        'hospital': v,
        'hospitalFilter': hospitalFilter,
    }
    return render(request, 'nursetemp/nview_hospital.html', context)


@login_required(login_url='login_view')
def add_complaint(request):
    form = Complaintnurse()
    u = request.user
    if request.method == 'POST':
        form = Complaintnurse(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, "Complaint Added Successfully")
            return redirect('nview_complaint')
    return render(request, 'nursetemp/nadd_complaint.html', {'form': form})


@login_required(login_url='login_view')
def nview_complaint(request):
    comp = Complaint.objects.filter(user=request.user)
    return render(request, 'nursetemp/nview_complaint.html', {'comp': comp})


@login_required(login_url='login_view')
def update_complaint(request,id):
    n = Complaint.objects.get(id=id)
    if request.method == 'POST':
        form = Complaintnurse(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Complaint Updated Successfully")
            return redirect('nview_complaint')
    else:
        form = Complaintnurse(request.POST or None, instance=n)
    return render(request, 'nursetemp/nupdate_complaint.html', {'form': form})


@login_required(login_url='login_view')
def complaint_delete(request,id):
    n = Complaint.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Hospital Deleted Successfully")
        return redirect('nview_complaint')
    else:
        return redirect('nview_complaint')


class Appointmentshedu:
    pass


@login_required(login_url='login_view')
def add_apposhedule(request):
    form = Appointmentshedu()
    if request.method == 'POST':
        form = Appointmentshedu(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Appointment Added Successfully")
            return redirect('view_shedule')
    return render(request, 'nursetemp/add_appointment.html', {'form': form})


@login_required(login_url='login_view')
def view_shedule(request):
    appo = Appointmentshedu.objects.all()
    return render(request, 'nursetemp/view_shedule.html', {'appo': appo})


@login_required(login_url='login_view')
def appo_update(request,id):
    n = Appointmentshedu.objects.get(id=id)
    if request.method == 'POST':
        form = Appointmentshedu(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Complaint Updated Successfully")
            return redirect('view_shedule')
    else:
        form = Appointmentshedu(request.POST or None, instance=n)
    return render(request, 'nursetemp/appo_update.html', {'form': form})


@login_required(login_url='login_view')
def appo_delete(request,id):
    n = Appointmentshedu.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Hospital Deleted Successfully")
        return redirect('view_shedule')
    else:
        return redirect('view_shedule')


@login_required(login_url='login_view')
def view_appointment(request):
    a = Appointment.objects.filter(status=1).order_by('schedule__hospital')
    return render(request, 'nursetemp/nview_appointment.html', {'appoint': a})


# def approve_vaccine(request, id):
#     n = Appointment.objects.get(id=id)
#     n.status = 1
#     n.save()
#     return redirect(request, 'usertemp/nview_appointment.html')

# def vaccine_approve(request,id):
#     appoint = Appointment.objects.get(id=id)
#     appoint.vaccinated=True
#     appoint.save()
#     return redirect('nview_appointment')


@login_required(login_url='login_view')
def mark_vaccinated(request, id):
    a = Appointment.objects.get(id=id)
    vaccine = Vaccine.objects.filter(approval_status=0)
    context = {
        'vaccine': vaccine,
        'a': a,
    }
    try:
        if request.method == 'POST':
            vacc = request.POST.get('vaccine')
            a.vaccinated = True
            a.vaccine_name = Vaccine.objects.get(id=vacc)
            a.save()
            return redirect('nview_appointment')
    except ValueError:
        messages.info(request, 'Please Select a Vaccine')
    return render(request, 'nursetemp/mark_vaccinated.html', context)


@login_required(login_url='login_view')
def nreport_add(request):
    form = Reportform()
    if request.method == 'POST':
        form = Reportform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Report Added Successfully")
            return redirect('nview_report')
    return render(request, 'nursetemp/nadd_report.html', {'form': form})


@login_required(login_url='login_view')
def nview_report(request):
    report = Report.objects.all()
    return render(request, 'nursetemp/nview_report.html', {'report': report})
