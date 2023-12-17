from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Doctor, Patient, Appointment, MedicalRecord

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {
            'classes': ('wide',),
            'fields': ('role',),
        }),
    )

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(CustomUser, CustomUserAdmin)
