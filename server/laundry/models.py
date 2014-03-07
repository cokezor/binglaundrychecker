from django.db import models

class Community(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Building(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	community = models.ForeignKey(Community, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Side(models.Model):
	name = models.CharField(max_length=40)
	locationId = models.CharField(max_length=10, blank=True)
	building = models.ForeignKey(Building, null=True)

	dryerTotal = models.IntegerField(blank=True)
	dryerAvail = models.IntegerField(blank=True)
	dryerTimes = models.CommaSeparatedIntegerField(max_length=20)
	dryerInUse = models.IntegerField(blank=True)

	washerTotal = models.IntegerField(blank=True)
	washerAvail = models.IntegerField(blank=True)
	washerTimes = models.CommaSeparatedIntegerField(max_length=20)
	washerInUse = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
