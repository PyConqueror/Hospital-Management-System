from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser, Patient, Doctor
from .forms import PatientSignUpForm, DoctorSignUpForm


def home(request):
    return render(request, 'home.html')

@login_required
def set_dashboard(request):
    user_role = request.user.role
    if user_role == 'doctor':
        return render(request, 'doctor/index.html')
    elif user_role == 'patient':
        return render(request, 'patient/index.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient/index.html')

def doctor_dashboard(request):
    return render(request, 'doctor/index.html')

def patient_signup(request):
    error_message = ''
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            Patient.objects.create(user=user)
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
            Doctor.objects.create(user=user)
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = DoctorSignUpForm()
    return render(request, 'registration/doctor_signup.html', {'form': form})