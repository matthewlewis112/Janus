from django.test import TestCase
from .models import ClassroomLeave, ClassroomReturn, StudentSession, Student
from .forms import LeaveForm, ReturnForm
import datetime

class LeaveFormTests (TestCase):
    def test_LeaveForm_valid1(self):
        form = LeaveForm(data={'Student_ID': 200})
        self.assertTrue(form.is_valid())

    def test_LeaveForm_valid2(self):
        form = LeaveForm(data={'Student_ID': 3})
        self.assertTrue(form.is_valid())

    def test_LeaveForm_invalid1(self):
        form = LeaveForm(data={'Student_ID': -1})
        self.assertFalse(form.is_valid())

    def test_LeaveForm_invalid2(self):
        form = LeaveForm(data={'Student_ID': "twelve"})
        self.assertFalse(form.is_valid())

    def test_LeaveForm_invalid3(self):
        form = LeaveForm()
        self.assertFalse(form.is_valid())


class ReturnFormTests (TestCase):
    def test_ReturnForm_valid1(self):
        form = ReturnForm(data={'Student_ID': 200})
        self.assertTrue(form.is_valid())

    def test_ReturnForm_valid2(self):
        form = ReturnForm(data={'Student_ID': 3})
        self.assertTrue(form.is_valid())

    def test_ReturnForm_invalid1(self):
        form = ReturnForm(data={'Student_ID': -1})
        self.assertFalse(form.is_valid())

    def test_ReturnForm_invalid2(self):
        form = ReturnForm(data={'Student_ID': "twelve"})
        self.assertFalse(form.is_valid())

    def test_ReturnForm_invalid3(self):
        form = ReturnForm()
        self.assertFalse(form.is_valid())


class LeaveModelTests (TestCase):
    def setUp(self):
        ClassroomLeave.objects.create(Student_ID = 123456, Leave_Time = datetime.datetime.now())
        ClassroomLeave.objects.create(Student_ID = 123457, Leave_Time = datetime.datetime.now() - datetime.timedelta(minutes = 67) )

    def test_FindClassroomLeave(self):
        obj1 = ClassroomLeave.objects.filter(Student_ID = 123456).get()
        self.assertTrue(obj1.Student_ID == 123456)
        obj2 = ClassroomLeave.objects.filter(Student_ID = 123457).get()
        self.assertTrue(obj2.Student_ID == 123457)

    def test_BadStudentID(self):
        with self.assertRaises(ValueError):
            ClassroomLeave.objects.create(Student_ID = "Dog")
        with self.assertRaises(ValueError):
            ClassroomLeave.objects.create(Student_ID = -5)
        with self.assertRaises(ValueError):
            ClassroomLeave.objects.create(Student_ID = None, Leave_Time = datetime.datetime.now())

    def test_BadLeaveTime(self):
        with self.assertRaises(ValueError):
            ClassroomLeave.objects.create(Student_ID = 3, Leave_Time = "string")
        with self.assertRaises(ValueError):
            ClassroomLeave.objects.create(Student_ID = 3, LeaveTime = 7)
