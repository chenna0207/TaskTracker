# Generated by Django 5.0.7 on 2024-07-16 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskTrackerApp', '0004_alter_customuser_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprojectrole',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TaskTrackerApp.customuser'),
        ),
    ]
