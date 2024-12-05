from django.db import models


# Create your models here.
class Instructor(models.Model):
  instructor_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return f'Instructor: {self.first_name} {self.last_name}'
