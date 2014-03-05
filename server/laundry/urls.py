from django.conf.urls import patterns, url

urlpatterns = patterns('laundry.views',
	url(r'^status/(?P<name>\w+)/$', 'machine_status'),
)
