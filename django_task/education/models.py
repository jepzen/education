from __future__ import unicode_literals

from django.db import models

# Create your models here.

class School(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Classroom(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	identifier = models.CharField(max_length=20)

	def __str__(self):
		return self.identifier
	
class Student(models.Model):
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
