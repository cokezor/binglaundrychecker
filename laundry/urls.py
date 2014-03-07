from django.conf.urls import patterns, url

urlpatterns = patterns('laundry.views',
	url(r'^buildings/(?P<name>\w+)/$', 'get_buildings'),
	url(r'^communities', 'get_communities'),
	url(r'^status/(?P<name>\w+)/?', 'get_laundry_status'),
)
