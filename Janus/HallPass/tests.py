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
