from django.urls import path
#api req 
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('employees/', views.employeeList.as_view()),
    path('table/', views.view_list)

]
