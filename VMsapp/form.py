import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from VMsapp.models import Nurse, User, Hospital, Appointment, Complaint, Vaccine, Report,\
    Appointmentschedule, Login


def phone_number_validator(value):
    if not re.compile(r'[0-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class Nurse_register(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Nurse
        exclude = ('user',)

    def clean_email(self):
        email = self.cleaned_data['email']
        email_qs = Nurse.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already registered")

        return email


class Userform(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = User
        exclude = ('user',)

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email already registered")
    #
    #     return email
    #


class Hospitalform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospital_name', 'place', 'contact_no', 'email')


class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('schedule', 'status', 'vaccine_name', 'vaccinated')


class Complaintform(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('reply',)


class Vaccineform(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('vaccine_name', 'vaccine_type', 'description')


class Reportform(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('patient', 'vaccine', 'date', 'time')


class Complaintnurse(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject', 'complaint', 'date')


class Complaintuser(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject', 'complaint', 'date')


class Appointmentshedu(forms.ModelForm):
    class Meta:
        model = Appointmentschedule
        fields = ('hospital', 'date', 'start_time', 'end_time')
