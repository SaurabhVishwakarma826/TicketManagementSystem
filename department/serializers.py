# department/serializers.py
from rest_framework import serializers
from .models import Department, DynamicFormData

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class DynamicFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicFormData
        fields = ('id', 'department', 'form_structure', 'submission_data', 'created_at')
