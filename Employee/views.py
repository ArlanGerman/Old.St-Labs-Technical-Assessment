from rest_framework import generics
from rest_framework import filters
from . import serializers
from . import models

# Create your views here.


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.EmployeeModel.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = (filters.OrderingFilter, )
    ordering_fields = ('monthly_salary', 'birth_date',
                       'first_name', 'last_name')


class EmployeeRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EmployeeModel.objects.all()
    serializer_class = serializers.EmployeeSerializer
