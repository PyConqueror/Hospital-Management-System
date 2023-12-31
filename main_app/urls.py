from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('appointment/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment_detail'),
    path('doctor/appointment/<int:pk>/', views.DoctorAppointmentDetail.as_view(), name='doctor_appointment_detail'),
    path('manager/appointment/<int:pk>/', views.ManagerAppointmentDetail.as_view(), name='manager_appointment_detail'),
    path('appointment/<int:pk>/edit/', views.AppointmentUpdate.as_view(), name='appointment_edit'),
    path('patient/appointment_request/', views.AppointmentRequest.as_view(), name='appointment_request_create'),
    path('patient/medical_records/', views.patient_medical_records, name='patient_medical_records'),
    path('patient/medical_records/<int:pk>/', views.MedicalRecordDetail.as_view(), name='medical_record_detail'),
    path('patient/profile/', views.PatientProfile.as_view(), name='patient_profile'),
    path('patient/profile/edit', views.PatientProfileUpdate.as_view(), name='patient_profile_edit'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/completed_appointment/', views.doctor_completed_appointment, name='completed_appoinments'),
    path('doctor/appointment/<int:pk>/edit/', views.DoctorAppointmentEdit.as_view(), name='doctor_appointment_edit'),
    path('appointment/<int:pk>/medical_record/', views.MedicalRecordCreate.as_view(), name='medical_record_create'),
    path('medical_records/<int:pk>/edit', views.EditMedicalRecord.as_view(), name='medical_record_edit'),
    path('doctor/my_patients/', views.doctor_patients, name='doctor_patients'),
    path('doctor/patient/<int:pk>/', views.PatientDetail.as_view(), name='patient_detail'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/appointment/<int:pk>/edit/', views.ManagerAppointmentEdit.as_view(), name='manager_appointment_edit'),
    path('manager/past_appoinment/', views.manager_past_appointment, name='manager_past_appointment'),
    path('manager/search_patients/', views.search_patients, name='search_patients'),
    path('manager/all_patients/', views.all_patients, name='all_patients'),
    path('manager/patient/<int:pk>/', views.ManagerPatientDetail.as_view(), name='manager_patient_detail'),
    path('manager/manage_doctors/', views.manage_doctors, name='manage_doctors'),
    path('manager/doctor_detail/<int:pk>/', views.DoctorDetail.as_view(), name='doctor_detail'),
    path('manager/doctor/<int:pk>/edit_status/', views.DoctorStatusUpdate.as_view(), name='edit_doctor_status'),

    # path('manager/appointment_requests/', views.appointment_requests, name='appointment_requests'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
    path('accounts/login/dashboard', views.set_dashboard, name='dashboard'),
    ]
 