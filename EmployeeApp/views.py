from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

@csrf_exempt
def department_get(request):
    departments = Departments.objects.all()
    departments_serializer = DepartmentSerializer(departments, many=True)
    return JsonResponse(departments_serializer.data, safe=False)

@csrf_exempt
def department_detail(request, id):
    try:
        department = Departments.objects.get(department_id=id)
        department_serializer = DepartmentSerializer(department)
        return JsonResponse(department_serializer.data, safe=False)
    except Departments.DoesNotExist:
        return JsonResponse("Department does not exist", status=404, safe=False)

@csrf_exempt
def department_post(request):
    departments_data = JSONParser().parse(request)
    departments_serializer = DepartmentSerializer(data=departments_data)
    if departments_serializer.is_valid():
        departments_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to add", safe=False)

@csrf_exempt
def department_update(request, id):
    try:
        department = Departments.objects.get(department_id=id)
    except Departments.DoesNotExist:
        return JsonResponse("Department does not exist", status=404, safe=False)

    if request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(department_serializer.errors, status=400, safe=False)
    else:
        return JsonResponse("PUT method is required", status=400, safe=False)

@csrf_exempt
def department_delete(request, id):
    try:
        department = Departments.objects.get(department_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully", status=200, safe=False)
    except Departments.DoesNotExist:
        return JsonResponse("Department does not exist", status=404, safe=False)

@csrf_exempt
def employee_get(request):
    employees = Employees.objects.all()
    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)

@csrf_exempt
def employee_detail(request, id):
    try:
        employee = Employees.objects.get(employee_id=id)
        employee_serializer = EmployeeSerializer(employee)
        return JsonResponse(employee_serializer.data, safe=False)
    except Employees.DoesNotExist:
        return JsonResponse("Employee does not exist", status=404, safe=False)

@csrf_exempt
def employee_post(request):
    employee_data = JSONParser().parse(request)
    employees_serializer = EmployeeSerializer(data=employee_data)
    if employees_serializer.is_valid():
        employees_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to add", safe=False)

@csrf_exempt
def employee_update(request, id):
    try:
        employee = Employees.objects.get(employee_id=id)
    except Employees.DoesNotExist:
        return JsonResponse("Employee does not exist", status=404, safe=False)

    if request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(employee_serializer.errors, status=400, safe=False)
    else:
        return JsonResponse("PUT method is required", status=400, safe=False)

@csrf_exempt
def employee_delete(request, id):
    try:
        employee = Employees.objects.get(employee_id=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", status=200, safe=False)
    except Employees.DoesNotExist:
        return JsonResponse("Employee does not exist", status=404, safe=False)