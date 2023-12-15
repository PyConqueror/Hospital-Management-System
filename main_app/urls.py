from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('dashboard/', views.set_dashboard, name='dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    # path('patient/medical_history/', views.patient_medical_history, name='patient_medical_history'),
    # path('patient/profile/', views.patient_profile, name='patient_profile'),
    # path('patient/appointment_request/', views.appointment_request, name='appointment_request'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    # path('doctor/my_patients/', views.my_patients, name='my_patients'),
    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('admin/manage_doctors/', views.manage_doctors, name='manage_doctors'),
    # path('admin/appointment_requests/', views.appointment_requests, name='appointment_requests'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
    path('accounts/login/dashboard', views.set_dashboard, name='dashboard')
    ]
 