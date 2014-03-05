from django.core.management.base import BaseCommand, CommandError
import requests
import re
from lxml import html
from laundry.models import Building
#custom command to scrape the buildings on a weekly(?) basis
class Command(BaseCommand):
	def handle(self, *args, **options):
		#load the page
		page = requests.get('http://binghamton-asi.esuds.net/RoomStatus/showRoomStatus.i?locationId=6788')

		#parse the html so we can use xpath
		tree = html.fromstring(page.text)
		building_list = tree.xpath('//li/a')

		#regex for matching the location id of each building
		#example: 'showRoomStatus.i?locationId=1008750'
		regex = re.compile('\d+')

		for item in building_list:
			locationId = regex.search(item.attrib['href']).group()
			building, created = Building.objects.get_or_create(name=item.text, locationId=locationId)
