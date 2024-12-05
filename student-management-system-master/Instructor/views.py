from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import InstructorForm
from .models import Instructor


# Create your views here.
def instructor_index(request):
    return render(request, 'Instructor/instructor_index.html', {
    'instructors': Instructor.objects.all()
  })

def view_instructor(request, id):
  return HttpResponseRedirect(reverse('index'))

def instructor_add(request):
  if request.method == 'POST':
    form = InstructorForm(request.POST)
    if form.is_valid():
      new_instructor_number = form.cleaned_data['instructor_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']

      new_instructor = Instructor(
        instructor_number=new_instructor_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
      )
      new_instructor.save()
      return render(request, 'Instructor/instructor_add.html', {
        'form': InstructorForm(),
        'success': True
      })
  else:
      form = InstructorForm()
  return render(request, 'Instructor/instructor_add.html', {
      'form': InstructorForm()
  })
def instructor_edit(request, id):
  if request.method == 'POST':
    instructor = Instructor.objects.get(pk=id)
    form = InstructorForm(request.POST, instance=instructor)
    if form.is_valid():
      form.save()
      return render(request, 'Instructor/instructor_edit.html', {
        'form': form,
        'success': True
      })
  else:
    instructor = Instructor.objects.get(pk=id)
    form = InstructorForm(instance=instructor)
  return render(request, 'Instructor/instructor_edit.html', {
    'form': form
  })


def instructor_delete(request, id):
  if request.method == 'POST':
    instructor = Instructor.objects.get(pk=id)
    instructor.delete()
  return HttpResponseRedirect(reverse('instructor_index'))