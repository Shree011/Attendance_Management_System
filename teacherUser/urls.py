from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('attendance', views.attendance, name='attendance'),
    path('records', views.records, name='records'),
    path('viewStudAtten/<str:pkey>', views.viewStudentAtten, name='viewStudentAtten'),
    path('logout', views.logout, name='logout')
]