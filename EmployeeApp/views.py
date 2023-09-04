from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employee
from  EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            departments = Departments.objects.all()
            department_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(department_serializer.data, safe=False)
        else:
            departments = Departments.objects.filter(DepartmentId=id)
            department_serializer = DepartmentSerializer(departments, many=True)
            response = JsonResponse(department_serializer.data, safe=False)
            if not isinstance(response, dict):
                return JsonResponse("NO DATA FOUND",safe=False)
            else:
                return JsonResponse(department_serializer.data, safe=False)
            


    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add")

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successful",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == "DELETE":
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def employeeApi(request,id):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees,many=True)
        return  JsonResponse(employee_serializer.data,safe=False)

    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add")

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId = employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successful",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == "DELETE":
        employee = Employee.objects.get(DepartmentId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)