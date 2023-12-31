# Generated by Django 5.0 on 2023-12-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_patient_emergency_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_and_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
