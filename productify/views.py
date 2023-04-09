from django.shortcuts import render

# Create your views here.

#importing required entities 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from . models import Employee
from .serializers import employeeSerializer

#class based view 
class employeeList(APIView):
    #get function
    def get(self, request):
        employees1 = Employee.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        pass
#for frontend 
def view_list(request):
    return render(request, 'index.html')
    