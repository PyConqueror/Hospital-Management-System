# Generated by Django 5.0 on 2023-12-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='emergency_contact',
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
