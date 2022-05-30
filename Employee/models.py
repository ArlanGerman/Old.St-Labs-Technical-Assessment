from turtle import update
from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameModel(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=256)
    last_name = models.CharField(blank=False, null=False, max_length=256)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        INACTIVE = 'INACTIVE', _('Inactive')

    status = models.CharField(
        blank=False, null=False, max_length=8, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        abstract = True


class SalaryModel(models.Model):
    monthly_salary = models.FloatField(blank=False, null=False, validators=(
        validators.MinValueValidator(10_000), validators.MaxValueValidator(100_000), ))

    class Meta:
        abstract = True


class EmployeeModel(BaseModel, NameModel, StatusModel, SalaryModel):
    employee_id = models.BigAutoField(primary_key=True)
    birth_date = models.DateField(blank=False, null=False)

    class Meta:
        unique_together = ('first_name', 'last_name', 'birth_date')

    @staticmethod
    def get_required_fields():
        return ('employee_id', 'first_name', 'last_name', 'birth_date', 'monthly_salary', 'status')
