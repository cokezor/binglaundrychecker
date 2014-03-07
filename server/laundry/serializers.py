from rest_framework import serializers
from laundry.models import Building, Community, Side

class CommunitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Community
		fields = ('name',)

class SideSerializer(serializers.ModelSerializer):
	class Meta:
		model = Side
		fields = ('name', 'washerTotal', 'washerAvail', 'washerInUse', 'washerTimes', 'dryerTotal', 'dryerAvail', 'dryerInUse', 'washerTimes')

class BuildingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Building
		fields = ('name',)
