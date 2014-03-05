from django.core.management.base import BaseCommand, CommandError
import requests
import re
from lxml import html
from laundry.models import Building, Side
from django.conf import settings

ROOMSTATUS_BASE_URL = getattr(settings, "ROOMSTATUS_BASE_URL", None)

#custom command that iterates through all of the communities and generates their buildings class Command(BaseCommand):
class Command(BaseCommand):
	def handle(self, *args, **options):
		buildings = Building.objects.all()

		for building in buildings:
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
				if created:
					building.side_set.add(side)
