from django import forms

from .models import Instructor


class InstructorForm(forms.ModelForm):
  class Meta:
    model = Instructor
    fields = ['instructor_number', 'first_name', 'last_name', 'email']

    labels = {
      'instructor_number': 'Instructor No.',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
    }
    widgets = {
      'instructor_number': forms.NumberInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'}),
      'first_name': forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'}),
      'last_name': forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'}),
      'email': forms.EmailInput(attrs={'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'}),
    }

