from django.contrib import admin

from adminUser.models import Attendance, Student, Subject, Teacher

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Subject)