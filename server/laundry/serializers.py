from rest_framework import serializers
from laundry.models import Building, Community, Machine

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Building
		fields = ('name',)

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Community
		fields = ('name', 'machines')

class MachineSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Machine
		fields = ('name')
