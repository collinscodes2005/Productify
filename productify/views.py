
#importing required entities
from django.shortcuts import render, redirect
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee, client, task
from .serializers import employeeSerializer, clientSerializer, taskSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#Login view
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['user_name']
            password = serializer.validated_data['password']
            try:
                client_obj = client.objects.get(user_name=username, password=password)

                #generating refresh and access token for the user that just logged into the system now 
                refresh_token = RefreshToken.for_user(client_obj)
                refresh = str(refresh_token)

                #refresh token
                access_token = refresh_token.access_token
                access = str(access_token)
                print("Login sucessful")
             

                return Response({'success': 'Login worked', 'refresh' : refresh, 'access': access}, status=status.HTTP_200_OK)
            except client.DoesNotExist:
                print("Login Failed")
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
          #  return Response({'success': 'Logged in successfully'}, status=status.HTTP_200_OK)
            return redirect('table')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#class based view
class employeeList(APIView):

  #  authentication_classes = [JWTAuthentication]


    #restricting the access:
   # permission_classes = [IsAuthenticated]

    #to perform read operations on the api
    def get(self, request):
        employees1 = Employee.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        print("Get successful")
        return Response(serializer.data, status=status.HTTP_200_OK)

    #to perform create operations on the api
    def post(self, request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete the particular api 
    def delete(self, request, pk):
        try:
            task_entry = Task.objects.get(pk=pk)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##view to refresg tghe access tokens for ysers 
class Taskview(APIView):
    def get(self, request):
        task1 = task.objects.all()
        serializer = taskSerializer(task1, many=True)
        print("Get successful")
        return Response(serializer.data, status=status.HTTP_200_OK)

    #to perform create operations on the api
    def post(self, request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#sign up view
class SignUpView(APIView):
    def post(self, request):
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User created successfully'}, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

#for frontend
def view_list(request):
    return render(request, 'index.html')

#for creatign employee
def create(request):
    return render(request, 'create.html')

#renders login page
def log(request):
    return render(request, "login.html")

#renders the signup page
def up(request):
    return render(request, "signup.html")