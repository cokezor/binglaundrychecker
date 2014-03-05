from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from laundry.serializers import BuildingSerializer, CommunitySerializer, SideSerializer
from laundry.models import Community, Side, Building
from django.http import HttpResponse

class JSONResponse(HttpResponse):
	"""
	Http response that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

class BuildingViewSet(viewsets.ModelViewSet):
	queryset = Building.objects.all()
	serializer_class = BuildingSerializer

class CommunityViewSet(viewsets.ModelViewSet):
	queryset = Community.objects.all()
	serializer_class = CommunitySerializer

class SideViewSet(viewsets.ModelViewSet):
	queryset = Side.objects.all()
	serializer_class = SideSerializer

def machine_status(request, building):
	if request.method == 'GET':

