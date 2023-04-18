from django.urls import path
#api req
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('employees/', views.employeeList.as_view(), name="api"),
    path('table/', views.view_list, name="table"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('create/', views.create, name='create'),
    path('log/', views.log, name="log"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('up/', views.up, name="up"),
    path('tasks/', views.Taskview().as_view()),
    path('task/<int:pk>/delete', views.deleteTask().as_view()),
    
]


