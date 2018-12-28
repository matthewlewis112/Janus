from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LeaveForm, ReturnForm
from .models import ClassroomLeave, ClassroomReturn, StudentSession
import datetime


# Create your views here.
def hallPassHome(request):
    return render(request, 'html/HallPassHome.html', {})


def leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.Leave_Time = datetime.datetime.now()
            form.save()
            return HttpResponseRedirect('Submitted/')
    else:
        form = LeaveForm()
    return render(request, 'html/HallPassForm.html', {'form': form})


def returning(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.Return_Time = datetime.datetime.now()
            form.save()
            createSession(form['Student_ID'].value())
            return HttpResponseRedirect('Submitted/')
    else:
        form = ReturnForm()
    return render(request, 'html/HallPassForm.html', {'form': form})


def submitted(request):
    return render(request, 'html/Submitted.html', {})


def createSession(StudentID):
    # Uses a student id to create a session
    Leave = ClassroomLeave.objects.filter(Student_ID = StudentID).get()
    Return = ClassroomReturn.objects.filter(Student_ID = StudentID).get()
    if Return:
        newSession = StudentSession()
        if Leave:
            # Create a session that contains leave and return times
            newSession.Student_ID = StudentID
            newSession.Leave_Time = Leave.Leave_Time
            newSession.Return_Time = Return.Return_Time
            newSession.save()
            # Remove the leave from the database
            Leave.delete()
        if Leave is None:
            # If there is not instance of the student leaving the class,
            # the system assumes that they left at the same time
            newSession.Student_ID = StudentID
            newSession.Leave_Time = Return.Return_Time
            newSession.Return_Time = Return.Return_Time
            newSession.save()
        # Remove the return from the database
        Return.delete()

    return




