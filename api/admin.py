from django.contrib import admin
from .models import Student,School

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Student Fields', {
            'fields': ('student_name', 'student_class', 'Student_roll_no')
        }),
        ('Other Fields', {            
            'fields': ('student_registration_no','student_subject','student_school_name'),
        }),
    )

class SchoolAdmin(admin.ModelAdmin):
     fieldsets = (
        ('List Of Schools', {
            'fields': ['schools_list']
        }),
     )

admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)

