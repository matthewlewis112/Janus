from django.contrib import admin
from .models import ClassroomLeave, ClassroomReturn, StudentSession, Student

# Register your models here.
admin.site.register(ClassroomLeave)
admin.site.register(ClassroomReturn)
admin.site.register(StudentSession)
admin.site.register(Student)

