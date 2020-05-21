from rest_framework import viewsets

from .serializers import StudentSerializer, SchoolSerializer
from .models import Student, School

class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all().order_by('Student_roll_no')
    serializer_class = StudentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer