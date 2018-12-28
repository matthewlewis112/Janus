from django.forms import ModelForm
from .models import ClassroomLeave, ClassroomReturn


class LeaveForm(ModelForm):
    class Meta:
        model = ClassroomLeave
        exclude = ['Leave_Time']


class ReturnForm(ModelForm):
    class Meta:
        model = ClassroomReturn
        exclude = ['Return_Time']
