from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from laundry.serializers import BuildingSerializer, LaundryRoomSerializer, MachineSerializer
from laundry.models import LaundryRoom, Machine, Building

class BuildingViewSet(viewsets.ModelViewSet):
	queryset = Building.objects.all()
	serializer_class = BuildingSerializer

class LaundryRoomViewSet(viewsets.ModelViewSet):
	queryset = LaundryRoom.objects.all()
	serializer_class = LaundryRoomSerializer

class MachineViewSet(viewsets.ModelViewSet):
	queryset = Machine.objects.all()
	serializer_class = MachineSerializer

