from django.urls import path

from VMsapp import views, nurse_views, user_views

urlpatterns = [

    path('', views.main_home, name='main_home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('login_page/', views.login_view, name='login_page'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('nursereg_form/', views.nurse_register, name='nursereg_form'),
    path('userreg_form/', views.user_register, name='userreg_form'),

    path('view_nurse/', views.view_nurse, name='view_nurse'),
    path('nurse_delete/<int:user_id>/', views.nurse_delete, name='nurse_delete'),
    path('view_user/', views.user, name='view_user'),
    path('user_delete/<int:id>/', views.user_delete, name='user_delete'),
    path('view_hospital/', views.hospital, name='view_hospital'),
    path('hospital_update/<int:id>/', views.update_hospital, name='hospital_update'),
    path('hospital_delete/<int:id>/', views.hospital_delete, name='hospital_delete'),
    path('complaint_view/', views.complaint_view, name='complaint_view'),
    path('add_hospital/', views.hospital_add, name='add_hospital'),
    path('appointment_shedule/', views.Approving_apnmt, name='appointment_shedule'),
    path('view_appointment/', views.appointment_view, name='view_appointment'),
    path('vaccine_approve//<int:id>', views.appointment_view, name='vaccine_approve'),
    path('approve_appoint/<int:id>/', views.approve_appoint, name='approve_appoint'),
    path('reject_appoint/<int:id>/', views.reject_appoint, name='reject_appoint'),
    path('comp_reply/<int:id>/', views.complaint_reply, name='comp_reply'),
    path('add_vaccine/', views.vaccine_add, name='add_vaccine'),
    path('view_vaccine/', views.view_vaccine, name='view_vaccine'),
    path('update_vaccine/<int:id>/', views.vaccine_update, name='update_vaccine'),
    path('delete_vaccine/<int:id>/', views.vaccine_delete, name='delete_vaccine'),
    path('view_report/', views.view_report, name='view_report'),

    path('nurse_home/', nurse_views.nurse_home, name='nurse_home'),

    path('nview_user/', nurse_views.view_user, name='nview_user'),
    path('nview_vaccine/', nurse_views.view_vaccine, name='nview_vaccine'),
    path('nview_hospital/', nurse_views.view_hospital, name='nview_hospital'),
    path('nadd_complaint/', nurse_views.add_complaint, name='nadd_complaint'),
    path('nview_complaint/', nurse_views.nview_complaint, name='nview_complaint'),
    path('nupdate_complaint/<int:id>/', nurse_views.update_complaint, name='nupdate_complaint'),
    path('ndelete_complaint/<int:id>/', nurse_views.complaint_delete, name='ndelete_complaint'),
    path('add_appointment/', nurse_views.add_apposhedule, name='add_appointment'),
    path('view_shedule/', nurse_views.view_shedule, name='view_shedule'),
    path('appo_update/<int:id>/', nurse_views.appo_update, name='appo_update'),
    path('appo_delete/<int:id>/', nurse_views.appo_delete, name='appo_delete'),
    path('nview_appointment/', nurse_views.view_appointment, name='nview_appointment'),
    path('mark_vaccinated/<int:id>/', nurse_views.mark_vaccinated, name='mark_vaccinated'),
    path('nadd_report/', nurse_views.nreport_add, name='nadd_report'),
    path('nview_report/', nurse_views.nview_report, name='nview_report'),

    path('user_home/', user_views.user_home, name='user_home'),
    path('reg_form/', user_views.reg_form, name='reg_form'),

    path('user_view/', user_views.profile_view, name='user_view'),
    path('profile_update/<int:user_id>/', user_views.profile_update, name='profile_update'),
    path('schedule_user/', user_views.schedule_user, name='schedule_user'),
    path('take_appointment/<int:id>/', user_views.take_appointment, name='take_appointment'),
    path('uview_appointment/', user_views.view_appoint, name='uview_appointment'),
    path('uadd_complaint/', user_views.uadd_complaint, name='uadd_complaint'),
    path('uview_complaint/', user_views.ucomplaint_view, name='uview_complaint'),
    path('uview_report/', user_views.view_report, name='uview_report'),
]
