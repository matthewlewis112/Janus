from django.db import models
import datetime


# Create your models here.
class ClassroomLeave(models.Model):
    Student_ID = models.IntegerField()
    Leave_Time = models.DateTimeField()

    def __str__(self):
        return str(self.Student_ID) + ' ' + str(self.Leave_Time)

    def save(self):
        if self.Leave_Time is None:
            self.Leave_Time = datetime.datetime.now()
        super(ClassroomLeave, self).save()


class ClassroomReturn(models.Model):
    Student_ID = models.IntegerField()
    Return_Time = models.DateTimeField()

    def __str__(self):
        return str(self.Student_ID) + ' ' + str(self.Return_Time)

    def save(self):
        if self.Return_Time is None:
            self.Return_Time = datetime.datetime.now()
        super(ClassroomReturn, self).save()


class StudentSession(models.Model):
    Student_ID = models.IntegerField()
    Leave_Time = models.DateTimeField()
    Return_Time = models.DateTimeField()

    def __str__(self):
        return str(self.Student_ID) + ' ' + str(self.Leave_Time)


class Student(models.Model):
    Student_ID = models.IntegerField()
    Student_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Student_Name
