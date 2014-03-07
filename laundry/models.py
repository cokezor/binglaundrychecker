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

	dryerTotal = models.IntegerField(blank=True, null=True)
	dryerAvail = models.IntegerField(blank=True, null=True)
	dryerTimes = models.CommaSeparatedIntegerField(max_length=20, null=True)
	dryerInUse = models.IntegerField(blank=True, null=True)

	washerTotal = models.IntegerField(blank=True, null=True)
	washerAvail = models.IntegerField(blank=True, null=True)
	washerTimes = models.CommaSeparatedIntegerField(max_length=20, null=True)
	washerInUse = models.IntegerField(blank=True, null=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
