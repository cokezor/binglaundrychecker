from rest_framework import serializers
from laundry.models import Building, Community, Side

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Building
		fields = ('name', 'sides')

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Community
		fields = ('name', 'buildings')

class SideSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Side
		fields = ('name',)
