from django.core.management.base import BaseCommand, CommandError
import requests
import re
from lxml import html
from laundry.models import Community
from django.conf import settings

ESUDS_BING_URL = getattr(settings, "ESUDS_BING_URL", None)

#custom command to scrape the communitys on a weekly(?) basis
class Command(BaseCommand):
	def handle(self, *args, **options):
		#load the page
		page = requests.get(ESUDS_BING_URL)

		#parse the html so we can use xpath
		tree = html.fromstring(page.text)
		community_list = tree.xpath('//li/a')

		#regex for matching the location id of each community
		#example: 'showRoomStatus.i?locationId=1008750'
		regex = re.compile('\d+')

		for item in community_list:
			locationId = regex.search(item.attrib['href']).group()
			community, created = Community.objects.get_or_create(name=item.text, locationId=locationId)
			print community
