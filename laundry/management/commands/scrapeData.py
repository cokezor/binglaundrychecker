from django.core.management.base import BaseCommand, CommandError
import requests
import re
from lxml import html
from laundry.models import Community, Building, Side
from django.conf import settings
from datetime import datetime
from time import sleep

ROOMSTATUS_BASE_URL = getattr(settings, "ROOMSTATUS_BASE_URL", None)
ESUDS_BING_URL = getattr(settings, "ESUDS_BING_URL", None)
SCRAPE_DAY = getattr(settings, "SCRAPE_DAY", None)

#custom command to scrape the communitys on a weekly(?) basis
class Command(BaseCommand):
	def handle(self, *args, **options):
		if datetime.today().isoweekday() != SCRAPE_DAY:
			print "NOT SCRAPE DAY"
			return

		#load the page
		page = requests.get(ESUDS_BING_URL)

		#parse the html so we can use xpath
		tree = html.fromstring(page.text)
		community_list = tree.xpath('//li/a')

		#regex for matching the location id of each community
		#example: 'showRoomStatus.i?locationId=1008750'
		regex = re.compile('\d+')

		#get all of the communities
		for item in community_list:
			locationId = regex.search(item.attrib['href']).group()
			community, created = Community.objects.get_or_create(name=item.text, locationId=locationId)
			print community

		count = 0
		#get all of the builidings
		communities = Community.objects.all()
		for community in communities:

			#dont request too quickly
			if count % 2 == 0:
				sleep(2)
			count += 1
			#load the page with the locationId
			page = requests.get(ROOMSTATUS_BASE_URL + community.locationId)

			#parse the html so we can use xpath
			tree = html.fromstring(page.text)
			laundry_links = tree.xpath('//span[@class="dormlinks"]/a')

			#regex for matching the location id of each building
			#example: 'showRoomStatus.i?locationId=1008750'
			regex = re.compile('\d+')

			for item in laundry_links:
				locationId = regex.search(item.attrib['href']).group()
				building, created = Building.objects.get_or_create(name=item.text, locationId=locationId)
				print building

				if created:
					community.building_set.add(building)


		#get all of the sides
		buildings = Building.objects.all()
		for building in buildings:

			if count % 3 == 0:
				sleep(2)

			count += 1
			#load the page with the locationId
			page = requests.get(ROOMSTATUS_BASE_URL + building.locationId)

			#parse the html so we can use xpath
			tree = html.fromstring(page.text)
			laundry_links = tree.xpath('//span[@class="laundrylinks"]/a')

			#regex for matching the location id of each building
			#example: 'showRoomStatus.i?locationId=1008750'
			regex = re.compile('\d+')

			for item in laundry_links:
				locationId = regex.search(item.attrib['href']).group()
				side, created = Side.objects.get_or_create(name=item.text, locationId=locationId)
				print side
				if created:
					building.side_set.add(side)
