from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment, MedicalRecord
from .forms import PatientSignUpForm, DoctorSignUpForm, AppointmentRequestForm, PatientProfileForm, AppointmentEditForm, AppointmentStatusUpdateForm, MedicalRecordForm

def home(request):
    return render(request, 'home.html')

@login_required
def set_dashboard(request):
    user_role = request.user.role
    if user_role == 'doctor':
        return redirect('doctor_dashboard')
    elif user_role == 'patient':
        return redirect('patient_dashboard')
    elif user_role == 'manager':
        return redirect('manager_dashboard')

@login_required
def patient_dashboard(request):
    user_role = request.user.role
    if user_role == 'patient':#route protection depends on role, other user type cannot access different dashboard
        current_appointments = Appointment.objects.filter(patient=request.user.patient_profile).exclude(status='completed').exclude(status='cancelled')
        appointment_request_form = AppointmentRequestForm()
        context = {
            'appointment_request_form': appointment_request_form,
            'current_appointments': current_appointments,
            }   
        return render(request, 'patient/index.html', context)
    else: 
        return redirect('dashboard')

def doctor_dashboard(request):
    user_role = request.user.role
    if user_role == 'doctor':
        scheduled_appointments = Appointment.objects.filter(  #show only the scheduled appointments for the logged in doctor
            doctor=request.user.doctor_profile, 
            status='scheduled'
        ).order_by('-date')
        completed_appointments = Appointment.objects.filter(
            doctor=request.user.doctor_profile, 
            status='completed'
        ).order_by('-date')
        context = {
            'scheduled_appointments': scheduled_appointments,
            'completed_appointments': completed_appointments,
        }
        return render(request, 'doctor/index.html', context)
    else:
        return redirect('dashboard')

def manager_dashboard(request):
    user_role = request.user.role
    if user_role == 'manager':
        appointment_requests = Appointment.objects.filter(status='pending').order_by('-date')
        past_appointments = Appointment.objects.exclude(status='pending').order_by('-date')
        doctors = Doctor.objects.all()
        context = {
            'appointment_requests': appointment_requests,
            'past_appointments': past_appointments,
            'doctors': doctors,
        }
        return render(request, 'manager/index.html', context)
    else: 
        return redirect('dashboard')

def patient_signup(request):
    error_message = ''
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            patient = Patient(
                user=user,
                name=form.cleaned_data.get('name'), 
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                gender=form.cleaned_data.get('gender'),
                address=form.cleaned_data.get('address'),
                phone_number=form.cleaned_data.get('phone_number'),
                emergency_contact=form.cleaned_data.get('emergency_contact'),
                medical_history=form.cleaned_data.get('medical_history') 
            )
            patient.save()
            login(request, user)
            return redirect('patient_dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = PatientSignUpForm()
    return render(request, 'registration/patient_signup.html', {'form': form})

def doctor_signup(request):
    error_message = ''
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'doctor'
            user.save()
            doctor = Doctor(
                user=user,
                name=form.cleaned_data.get('name'),  
                specialization=form.cleaned_data.get('specialization'),  
                years_of_experience=form.cleaned_data.get('years_of_experience'),
                contact_information=form.cleaned_data.get('contact_information')
            )
            doctor.save()
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = DoctorSignUpForm()
    return render(request, 'registration/doctor_signup.html', {'form': form})


class AppointmentRequest(CreateView):
    model = Appointment
    form_class = AppointmentRequestForm
    template_name = 'appointments/appointment_request_form.html'

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient_profile
        form.instance.status = 'pending'  # set the initial status to pending
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('patient_dashboard')  #redirect to the patient dashboard after successful submission
    
class AppointmentDetail(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentUpdate(UpdateView):
    model = Appointment
    form_class = AppointmentRequestForm
    template_name = 'appointments/appointment_form.html'

    def get_success_url(self):
        return reverse_lazy('appointment_detail', kwargs={'pk': self.object.pk})

class PatientProfile(DetailView):
    model = Patient
    template_name = 'patient/patient_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.patient_profile
    
class PatientProfileUpdate(UpdateView):
    model = Patient
    form_class = PatientProfileForm
    template_name = 'patient/patient_profile_edit.html'
    
    def get_object(self):
        return self.request.user.patient_profile

    def get_success_url(self):
        return reverse_lazy('patient_profile')

class ManagerAppointmentEdit(UpdateView):
    model = Appointment
    form_class = AppointmentEditForm
    template_name = 'appointments/manager_appointment_edit_form.html'

    def get_success_url(self):
        return reverse_lazy('manager_dashboard')
    
class DoctorAppointmentEdit(UpdateView):
    model = Appointment
    form_class = AppointmentStatusUpdateForm
    template_name = 'appointments/doctor_appointment_edit_form.html'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor_profile)

    def get_success_url(self):
        return reverse_lazy('doctor_dashboard')
    
class MedicalRecordCreate(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'doctor/new_medical_record_form.html'

    def form_valid(self, form):
        form.instance.appointment = Appointment.objects.get(pk=self.kwargs['pk']) #set the patient and doctor automatically based on the appointment
        form.instance.patient = form.instance.appointment.patient
        form.instance.doctor = self.request.user.doctor_profile
        form.instance.date_of_record = timezone.now().date()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('doctor_dashboard') #redirect back to dr dashboard after medical record is created

def patient_medical_records(request):
    medical_records = MedicalRecord.objects.filter(patient=request.user.patient_profile).order_by('-date_of_record')
    return render(request, 'patient/records.html', {'medical_records': medical_records})

class MedicalRecordDetail(DetailView):
    model = MedicalRecord
    template_name = 'patient/medical_record_detail.html'
    context_object_name = 'record'
