from datetime import date

from adminUser.models import Attendance, Student, Teacher
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *

def checkSessions(request):
    try:
        teach_username = request.session['teach_username']
        return teach_username
    except:
        return redirect('login')
    
# Create your views here.
def logout(request):
    try:
        del request.session['teach_username']
    except:
        pass
    return redirect('login')
def viewStudentAtten(request, pkey):
    teach_username =  checkSessions(request)
    records = Attendance.objects.filter(stud_id = pkey, teach_username = teach_username).order_by('atten_date')
    context = {
        'records' : records
    }
    return render(request, 'teacherUser/viewPersonalAttendance.html', context)

def records(request):
    teach_username =  checkSessions(request)
    #records = Attendance.objects.filter(teach_username = teach_username)
    if request.method == 'GET':
        present_attendance = []
        mainlist = []
        stud_class = request.GET.get('stud_class')
        records  = Student.objects.filter(stud_class = stud_class)
        total_attendance = Attendance.objects.filter(teach_username = teach_username).distinct('atten_date').count()
        for student in records:
            current_attendance = Attendance.objects.filter(teach_username = teach_username, stud_id_id = student.id, attendance='Present').count()
            list1 = [student.roll_no, student.stud_name, student.stud_class, current_attendance, student.id]
            #print(list1)
            mainlist.append(list1)
            
    context = {
        'records' : mainlist,
        'total_attendance' : total_attendance
    }
    return render(request, 'teacherUser/records.html', context)

def attendance(request):
    teach_username =  checkSessions(request)
    if request.method == 'POST':
        subject = Teacher.objects.filter(username = teach_username).values('subject')
        atten_date = request.POST['date']
        if atten_date == "":
            atten_date = date.today().strftime("%Y-%m-%d")
        if Attendance.objects.filter(atten_date=atten_date, teach_username=teach_username).exists():
            msg = 'attendence for ' + atten_date + ' is filled'
            messages.info(request, msg)
            return redirect('attendance')
        last = request.POST.getlist('last_roll[]')
        for a in last:
            attendance = 'attendance' + str(a)
            if request.POST[attendance] is None:
                messages.info(request, 'please enter all the details')
                return redirect('attendance')
            atten = request.POST[attendance]
            attendancee = Attendance(stud_id_id = a, attendance = atten, subject = subject, teach_username = teach_username, atten_date = atten_date)
            attendancee.save()
        messages.info(request, 'attendance saved')
        return redirect('attendance')
   
    data = Teacher.objects.all().filter(username=teach_username)
    if request.method == 'GET':
        classreq = request.GET.get('class')
        studentsData = Student.objects.filter(stud_class=classreq)
    else:
        studentsData = Student.objects.all()
    context = {
        'teach_username' : teach_username,
        'data' : data,
        'studentsData' : studentsData
    }
    return render(request, 'teacherUser/attendance.html', context)

def home(request):
    return render(request, 'teacherUser/teacher_home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        if Teacher.objects.filter(username=username, password=password).exists():
            data = Teacher.objects.all().filter(username=username)
            request.session['teach_username'] = username
            context = {
                'data' : data
            }
            return render(request, 'teacherUser/teacher_home.html', context) 
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'teacherUser/login.html')
