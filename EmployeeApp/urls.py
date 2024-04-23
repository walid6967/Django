from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('department/', views.department_get, name="department_get"),
    path('department/<int:id>/detail/', views.department_detail, name="department_detail"),
    path('department/create/', views.department_post, name="department_post"),
    path('department/<int:id>/update/', views.department_update, name="department_update"),
    path('department/delete/<int:id>/', views.department_delete, name="department_delete"),

    path('employee/', views.employee_get, name="employee_get"),
    path('employee/<int:id>/detail/', views.employee_detail, name="employee_detail"), 
    path('employee/create/', views.employee_post, name="employee_post"),
    path('employee/<int:id>/update/', views.employee_update, name="employee_update"),
    path('employee/delete/<int:id>/', views.employee_delete, name="employee_delete")
]