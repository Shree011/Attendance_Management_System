from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages

# Create your views here.
def addTeach(request):
    if request.method == 'POST':
        username = request.POST['username']
        teach_name = request.POST['teach_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_no = request.POST['phone_no']
        subject = request.POST['subject']

        if password1 == password2:
            if Teacher.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists')
            elif Teacher.objects.filter(email=email).exists():
                messages.info(request, 'Email Exists')
            else:
                teach = Teacher(username=username, password=password1, teach_name=teach_name, email=email, phone_no=phone_no, subject=subject)
                teach.save()
                messages.info(request, 'Teachers data saved')
        else:
            messages.info(request, 'passwords are not matching')

        return redirect('addTeach')
    else:
        return render(request, 'adminUser/addTeacher.html')

def addStud(request):
    
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        stud_name = request.POST['stud_name']
        phone_no = request.POST['phone_no']
        address = request.POST['address']
        stud_class = request.POST['stud_class']
        if Student.objects.filter(roll_no=roll_no, stud_class=stud_class).exists():
            messages.info(request, 'Duplicate roll no')
        else:
            student = Student(roll_no=roll_no, stud_name=stud_name, phone_no=phone_no, address=address, stud_class=stud_class)
            student.save()
            messages.info(request, 'Students data saved')
        return redirect('addStud')
    else:
        #return redirect('addStud')
        return render(request, 'adminUser/addStudent.html')

def teacherDet(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers' : teachers
    }
    return render(request, 'adminUser/teacherDetails.html', context)

def studentsDet(request):
    students = Student.objects.all()
    #print(students)
    context = {
        'students' : students
    }
    return render(request, 'adminUser/studentDetails.html', context)

def home(request):
    return render(request, 'adminUser/admin_home.html')

