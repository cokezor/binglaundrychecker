from rest_framework import serializers
from laundry.models import Building, LaundryRoom, Machine

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Building
		fields = ('name',)

class LaundryRoomSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LaundryRoom
		fields = ('name', 'machines')

class MachineSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Machine
		fields = ('name')
