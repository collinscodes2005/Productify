from rest_framework import serializers
from . models import Employee, client, task

#employeeSerializer
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id','first_name', 'last_name')

#clientSerializer
class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ('user_name', 'password')
#task serializer

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('id', 'text', 'reminder', 'day')