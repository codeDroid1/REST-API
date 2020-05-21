from django.db import models

class School(models.Model):
    schools_list = models.CharField(max_length=150)

    def __str__(self):
        return self.schools_list
    

class Student(models.Model):
    student_registration_no = models.IntegerField(default=0)
    student_name = models.CharField(max_length=150)
    student_class = models.CharField(max_length=20)
    Student_roll_no = models.IntegerField()
    student_subject = models.TextField()
    student_school_name = models.ForeignKey(School, on_delete=models.CASCADE, default="")
    

    def __str__(self):
        return self.student_name