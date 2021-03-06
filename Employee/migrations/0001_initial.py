# Generated by Django 4.0.4 on 2022-05-30 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=8)),
                ('monthly_salary', models.FloatField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000)])),
                ('employee_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
            ],
            options={
                'unique_together': {('first_name', 'last_name', 'birth_date')},
            },
        ),
    ]
