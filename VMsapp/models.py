from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    address = models.TextField()
    child_name = models.CharField(max_length=100)
    child_gender = models.CharField(max_length=100)
    child_age = models.CharField(max_length=100)
    recent_vaccinations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.hospital_name


class Nurse(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='nurse')
    name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='hospital')

    def __str__(self):
        return self.name


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.TextField(max_length=200, null=True, blank=True)


class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=100)
    vaccine_type = models.CharField(max_length=100)
    description = models.TextField()
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.vaccine_name


class Appointmentschedule(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Appointmentschedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, null=True, blank=True)
    vaccinated = models.BooleanField(default=False)


class Report(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='vaccine')
    date = models.DateField()
    time = models.TimeField()
    # pdf = models.FileField()
