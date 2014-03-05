from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from laundry.serializers import BuildingSerializer, CommunitySerializer, MachineSerializer
from laundry.models import Community, Machine, Building

class BuildingViewSet(viewsets.ModelViewSet):
	queryset = Building.objects.all()
	serializer_class = BuildingSerializer

class CommunityViewSet(viewsets.ModelViewSet):
	queryset = Community.objects.all()
	serializer_class = CommunitySerializer

class MachineViewSet(viewsets.ModelViewSet):
	queryset = Machine.objects.all()
	serializer_class = MachineSerializer

