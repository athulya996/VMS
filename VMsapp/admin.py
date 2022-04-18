from django.contrib import admin

# Register your models here.
from VMsapp import models

admin.site.register(models.Login)
admin.site.register(models.Nurse)
admin.site.register(models.User)
admin.site.register(models.Hospital)
admin.site.register(models.Complaint)
admin.site.register(models.Appointment)
admin.site.register(models.Vaccine)
admin.site.register(models.Appointmentschedule)
admin.site.register(models.Report)
