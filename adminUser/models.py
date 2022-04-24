from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    teach_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.teach_name


class Student(models.Model):
    roll_no = models.IntegerField()
    stud_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    stud_class = models.CharField(max_length=100)

    def __str__(self):
        return self.stud_name

class Attendance(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='atten')
    attendance = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    teach_username = models.CharField(max_length=100)
    atten_date = models.DateField()

    #def __str__(self):
        #return self.teach_username

    def __str__(self):
        return self.teach_username