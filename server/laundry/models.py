from django.db import models


class Machine(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class LaundryRoom(models.Model):
	name = models.CharField(max_length=40)
	machines = models.ManyToManyField(Machine)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Building(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	laundryRooms = models.ManyToManyField(LaundryRoom)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
