from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LeaveForm, ReturnForm
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
            return HttpResponseRedirect('/thanks/')
    else:
        form = LeaveForm()
    return render(request, 'html/HallPassForm.html', {'form': form})


def returning(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.Return_Time = datetime.datetime.now()
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ReturnForm()
    return render(request, 'html/HallPassForm.html', {'form': form})


