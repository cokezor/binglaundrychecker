from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from laundry.serializers import BuildingSerializer, CommunitySerializer, SideSerializer
from laundry.models import Community, Side, Building
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.conf import settings
import requests
import re
from lxml import html



MACHINESTATUS_BASE_URL  = getattr(settings, "MACHINESTATUS_BASE_URL", None)

class JSONResponse(HttpResponse):
	"""
	Http response that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def get_laundry_status(request, name):
	"""
	Get status of a building's laundry
	"""
	name = name.replace("_", " ")
	if name == "Johnson":
		name = "Johnson-Bing"
	building = Building.objects.get(name=name)
	sides = building.side_set.all()

	get_side_status(sides)
	serializer = SideSerializer(sides, many=True)
	return JSONResponse(serializer.data)

def get_side_status(sides):
	for side in sides:
		page = requests.get(MACHINESTATUS_BASE_URL + side.locationId)
		tree = html.fromstring(page.text)

		stats = tree.xpath('//script')[0].text
		regex = re.compile('"((?:washers|dryers)\w+)"\).\w+\("(\d+)"\)')

		for status in regex.findall(stats):
			if status[0] == 'washersAvailCount':
				side.washerAvail = int(status[1])
			elif status[0] == 'washersTotalCount':
				side.washerTotal = int(status[1])
			elif status[0] == 'dryersAvailCount':
				side.dryerAvail = int(status[1])
			elif status[0] == 'dryersTotalCount':
				side.dryerTotal = int(status[1])
		
		side.dryerInUse = 0
		side.dryerTimes = ""
		side.washerInUse = 0
		side.washerTimes = ""

		#if there are machines in use, we have to scrape the times
		if side.dryerAvail != side.dryerTotal or side.washerAvail != side.washerTotal:
			rows = tree.xpath('//tr[@class="even"] | //tr[@class="odd"]')
			dryerTimes = []
			washerTimes = []
			for row in rows:
				if row[3][0].text == "In Use":
					if row[2].text == "Dryer":
						side.dryerInUse += 1
						dryerTimes.append(row[4].text)
					else:
						side.washerInUse += 1
						washerTimes.append(row[4].text)

			side.dryerTimes = dryerTimes
			side.washerTimes = washerTimes

		side.save()
		"""
		for row in rows:
			machine_type, status, time = machine_info(row)
			if machine_type == "Washer":
				washerTotal += 1

				if status == "Available":
					washerAvail += 1
		"""

def get_buildings(request, name):
	"""
	Get all buildings for a community
	"""
	name = name.replace("_", " ")
	community = Community.objects.get(name=name)
	buildings = community.building_set.all()
	serializer = BuildingSerializer(buildings, many=True)
	return JSONResponse(serializer.data)

def get_communities(request):
	"""
	Return all communities
	"""
	communities = Community.objects.all()
	serializer = CommunitySerializer(communities, many=True)
	return JSONResponse(serializer.data)

