# department/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Department, DynamicFormData
from .serializers import DepartmentSerializer, DynamicFormDataSerializer

class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DynamicFormListView(generics.ListCreateAPIView):
    queryset = DynamicFormData.objects.all()
    serializer_class = DynamicFormDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class DynamicFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DynamicFormData.objects.all()
    serializer_class = DynamicFormDataSerializer
    permission_classes = [permissions.IsAuthenticated]
