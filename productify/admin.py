from django.contrib import admin
from . models import Employee, client
# Register your models here.

#registering the employee 
admin.site.register(Employee)
admin.site.register(client)
