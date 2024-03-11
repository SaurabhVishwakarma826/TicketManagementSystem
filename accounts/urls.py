from django.urls import path
from .views import RegisterUserView, LoginUserView, DummyRestrictedView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('dummy-restricted/', DummyRestrictedView.as_view(), name='dummy-restricted'),
]