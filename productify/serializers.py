from rest_framework import serializers
from . models import Employee

class employeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')
