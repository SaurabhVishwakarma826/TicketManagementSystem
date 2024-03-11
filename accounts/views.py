from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import CustomUserSerializer, CustomUserLoginSerializer
from .permissions import IsManager, IsMember
from rest_framework.views import APIView

class RegisterUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        department_data = self.request.data.get('department', {})
        department_name = department_data.get('name')
        if department_name:
            department_instance, created = Department.objects.get_or_create(name=department_name)
            serializer.save(department=department_instance)
        else:
            serializer.save()


class LoginUserView(generics.CreateAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve user instance from serializer's validated data
        user_data = serializer.validated_data
        user = get_user_model().objects.get(email=user_data['email'])

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class DummyRestrictedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if IsManager().has_permission(request, self):
            return Response({"message": "Welcome, Manager! You have access to this view."})
        elif IsMember().has_permission(request, self):
            return Response({"message": "Welcome, Member! You do not have access to this view."})
        else:
            return Response({"message": "Unknown role. Access denied."})