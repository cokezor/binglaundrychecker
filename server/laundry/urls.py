from django.conf.urls import patterns, url

urlpatterns = patterns('laundry.views',
	url(r'^status/(?P<name>\w+)/$', 'machine_status'),
	url(r'^get_buildings/(?P<name>\w+)/$', 'get_buildings'),
	url(r'^communities', 'get_communities'),
)
