from django.db import models

class Side(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Machine(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Building(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	machines = models.ManyToManyField(Side)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Community(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	buildings = models.ManyToManyField(Building)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
