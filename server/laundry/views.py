from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from laundry.serializers import BuildingSerializer, CommunitySerializer, SideSerializer
from laundry.models import Community, Side, Building
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
	"""
	Http response that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

class CommunityViewSet(viewsets.ModelViewSet):
	queryset = Community.objects.all()
	serializer_class = CommunitySerializer

class SideViewSet(viewsets.ModelViewSet):
	queryset = Side.objects.all()
	serializer_class = SideSerializer

def get_buildings(request, name):
	name = name.replace("_", " ")
	community = Community.objects.get(name=name)
	buildings = community.buildings.all()
	serializer = BuildingSerializer(buildings, many=True)
	return JSONResponse(serializer.data)

def machine_status(request, name):
	if request.method == 'GET':
		#do something
		pass

