# Generated by Django 5.0.1 on 2024-03-15 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0006_alter_appointment_spaciality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='spaciality',
            new_name='speciality',
        ),
    ]