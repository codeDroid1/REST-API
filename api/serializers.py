from rest_framework import serializers
from .models import Student, School
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_name', 'student_registration_no', 'student_class', 'Student_roll_no', 'student_subject','student_school_name')

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('schools_list', 'category')