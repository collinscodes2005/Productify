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
    
    #to perform read operations on the api
    def get(self, request):
        employees1 = Employee.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #to perform create operations on the api
    def post(self, request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#for frontend 
def view_list(request):
    return render(request, 'index.html')

#for creatign employee
def create(request):
    return render(request, 'create.html')