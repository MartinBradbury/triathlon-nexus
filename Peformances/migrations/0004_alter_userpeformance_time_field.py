# Generated by Django 5.0.6 on 2024-06-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peformances', '0003_alter_userpeformance_time_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpeformance',
            name='time_field',
            field=models.TimeField(default='00:00:00', help_text='Enter time in HH:MM:SS format'),
        ),
    ]
