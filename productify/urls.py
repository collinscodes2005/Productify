from django.urls import path
#api req 
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('employees/', views.employeeList.as_view(), name="api"),
    path('table/', views.view_list),
    path('create/', views.create, name='create')

]
