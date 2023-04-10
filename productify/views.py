from django.shortcuts import render

# Create your views here.

#importing required entities 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from . models import Employee, client
from .serializers import employeeSerializer, clientSerializer


#Login view 
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['user_name']
            password = serializer.validated_data['password']
            try:
                client_obj = client.objects.get(user_name=user_name, password=password)
            except client.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'success': 'Logged in successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

def log(request):
    return render(request, "login.html")
