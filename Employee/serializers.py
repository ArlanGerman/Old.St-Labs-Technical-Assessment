from rest_framework import serializers
from . import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeModel
        fields = models.EmployeeModel.get_required_fields()
