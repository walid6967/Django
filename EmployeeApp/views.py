from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer= DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method == 'POST':
        departments_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department_id = department_data.get('DepartmentID')
        if department_id is not None:
            try:
                department = Departments.objects.get(DepartmentID=department_id)
                departments_serializer = DepartmentSerializer(department, data=department_data)
                if departments_serializer.is_valid():
                    departments_serializer.save()
                    return JsonResponse("Updated Successfully", safe=False)
                return JsonResponse(departments_serializer.errors, status=400, safe=False)
            except Departments.DoesNotExist:
                return JsonResponse("Department does not exist", status=404, safe=False)
        else:
            return JsonResponse("DepartmentID is missing in the request data", status=400, safe=False)
    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentID=id)
            department.delete()
            return JsonResponse("Deleted Successfully", status=200, safe=False)
        except Departments.DoesNotExist:
            return JsonResponse("Department does not exist", status=404, safe=False)
            


@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer= EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method == 'POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
            employee_data = JSONParser().parse(request)
            employee_id = employee_data.get('EmployeeID')
            if employee_id is not None:
                try:
                    employee = Employees.objects.get(EmployeeID=employee_id)
                    employee_serializer = EmployeeSerializer(employee, data=employee_data)
                    if employee_serializer.is_valid():
                        employee_serializer.save()
                        return JsonResponse("Updated Successfully", safe=False)
                    return JsonResponse(employee_serializer.errors, status=400, safe=False)
                except Employees.DoesNotExist:
                    return JsonResponse("Employee does not exist", status=404, safe=False)
            else:
                return JsonResponse("EmployeeId is missing in the request data", status=400, safe=False)
        
    elif request.method == 'DELETE':
        employee= Employees.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Delted Successfully", safe=False)
