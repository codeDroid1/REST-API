from rest_framework import serializers
from .models import Student, School

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_name', 'student_registration_no', 'student_class', 'Student_roll_no', 'student_subject','student_school_name')

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['schools_list']