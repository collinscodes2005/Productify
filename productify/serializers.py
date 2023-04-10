from rest_framework import serializers
from . models import Employee, client

class employeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')

class clientSerializer(serializers.ModelSerializer):

    class Meta:
        model = client
        fields = ('user_name', 'password')
