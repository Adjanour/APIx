from rest_framework import serializers
from EmployeeApp.models import Departments,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')
        many=True



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId','EmployeeName','Department','DateofJoining','PhotoFileName')