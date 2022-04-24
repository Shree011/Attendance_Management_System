from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addStudentDetails', views.addStud, name="addStud"),
    path('addTeacherDetails', views.addTeach, name='addTeach'),
    path('teachersDetails', views.teacherDet, name='teacherDet'),
    path('studentDetails', views.studentsDet, name='studentDet')
]