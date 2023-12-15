from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class PatientSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, help_text='Enter your full name')
    date_of_birth = forms.DateField(help_text='Enter your date of birth')
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], help_text='Select your gender')
    address = forms.CharField(widget=forms.Textarea, help_text='Enter your address')
    phone_number = forms.CharField(max_length=15, help_text='Enter your phone number')
    emergency_contact = forms.CharField(widget=forms.Textarea, help_text='Enter your emergency contact details')
    medical_history = forms.CharField(widget=forms.Textarea, required=False, help_text='Enter your medical history')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'name', 'date_of_birth', 'gender', 'address', 'phone_number', 'emergency_contact', 'medical_history',)

class DoctorSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, help_text='Enter your full name')
    SPECIALIZATIONS = [
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('neurology', 'Neurology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('gastroenterology', 'Gastroenterology'),
        ('oncology', 'Oncology'),
        ('psychiatry', 'Psychiatry'),
        ('obgyn', 'OB/GYN'),
        ('endocrinology', 'Endocrinology'),
        ]
    specialization = forms.ChoiceField(choices=SPECIALIZATIONS, help_text='Select your specialization')
    years_of_experience = forms.IntegerField(min_value=0, help_text='Enter your years of experience')
    contact_information = forms.CharField(widget=forms.Textarea, help_text='Enter your contact information')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'name', 'specialization', 'years_of_experience', 'contact_information',)
