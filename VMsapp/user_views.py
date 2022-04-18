
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from VMsapp.filter import ScheduleFilter
from VMsapp.form import Appointmentshedu, Userform, Complaintuser
from VMsapp.models import User, Complaint, Appointment, Report


@login_required(login_url='login_view')
def user_home(request):
    return render(request, 'usertemp/user_home.html')


@login_required(login_url='login_view')
def schedule_user(request):
    s = Appointmentshedu.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=s)
    s = scheduleFilter.qs
    context = {
        'schedule': s,
        'scheduleFilter': scheduleFilter
    }
    return render(request, 'usertemp/schedule_user.html', context)


@login_required(login_url='login_view')
def profile_view(request):
    user = request.user
    profile = User.objects.filter(user=user)
    return render(request, 'usertemp/user_view.html', {'profile': profile})


@login_required(login_url='login_view')
def profile_update(request, user_id):
    n = User.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = Userform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Profile Updated Successfully")
            return redirect('user_view')
    else:
        form = Userform(request.POST or None, instance=n)
    return render(request, 'usertemp/profile_update.html', {'form': form})


@login_required(login_url='login_view')
def uadd_complaint(request):
    form = Complaintuser()
    u = request.user
    if request.method == 'POST':
        form = Complaintuser(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, "Complaint Added Successfully")
            return redirect('user_home')
    return render(request, 'usertemp/uadd_complaint.html', {'form': form})


@login_required(login_url='login_view')
def ucomplaint_view(request):
    comp = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/uview_complaint.html', {'comp': comp})


@login_required(login_url='login_view')
def reg_form(request):
    return render(request, 'usertemp/reg_form.html')


@login_required(login_url='login_view')
def take_appointment(request,id):
    schedule = Appointmentshedu.objects.get(id=id)
    user1 = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=user1, schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('schedule_user')
    if request.method == 'POST':
        obj = Appointment()
        obj.user = user1
        obj.schedule = schedule
        obj.save()
        messages.info(request, "Appointment Booked Successfully")
        return redirect('uview_appointment')
    return render(request, 'usertemp/take_appointment.html', {'schedule': schedule})


@login_required(login_url='login_view')
def view_appoint(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'usertemp/uview_appointment.html', {'appoint': a})


@login_required(login_url='login_view')
def view_report(request):
    u = User.objects.get(user=request.user)
    report = Report.objects.filter(patient=u)
    return render(request, 'usertemp/uview_report.html', {'report': report})
