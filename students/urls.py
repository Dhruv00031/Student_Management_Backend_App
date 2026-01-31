from django.urls import path
from .views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    #Backward compatibility while introducing versioned endpoints
    path('v1/students/', StudentListCreateView.as_view()),
    path('v1/students/<int:pk>/', StudentDetailView.as_view()),
]
