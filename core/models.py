from django.db import models
from django.contrib import admin

# Create your models here.
class SystemConfig(models.Model):
	key = models.CharField(max_length=16)
	value = models.TextField(max_length=65536)

	def __str__(self):
		return self.key

class Department(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField()
	color = models.CharField(max_length=16)
	image = models.ImageField()

	def __str__(self):
		return self.name

class ProgramGroup(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField()
	degree = models.CharField(max_length=64)
	code = models.CharField(max_length=8)
	color = models.CharField(max_length=16)
	image = models.ImageField()

	def __str__(self):
		return self.name

class Program(models.Model):
	name = models.CharField(max_length=128)
	group = models.ForeignKey('ProgramGroup', on_delete=models.CASCADE)
	department = models.ForeignKey('Department', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Staff(models.Model):
	name = models.CharField(max_length=128)
	role = models.CharField(max_length=128)
	room = models.ForeignKey('Room', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	@admin.display(description='Building')
	def building(self):
		return self.room.building

class Building(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Room(models.Model):
	name = models.CharField(max_length=64)
	building = models.ForeignKey('Building', on_delete=models.CASCADE)

	def __str__(self):
		return self.name
