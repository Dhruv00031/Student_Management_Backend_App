from rest_framework import generics, status, filters
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response

from .models import Student
from .permissions import IsAdminOrReadOnly
from .serializers import StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['name', 'roll_number', 'email']
    ordering_fields = ['name', 'year', 'created_at']
    ordering = ['-created_at']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "message": "Student created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self):
        try:
            return super().get_object()
        except Exception:
            raise NotFound("Student not found")

    def update(self, request, *args, **kwargs):
        if not request.data:
            raise ValidationError("Request body cannot be empty")
        return super().update(request, *args, **kwargs)
