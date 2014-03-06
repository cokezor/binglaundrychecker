from django.conf.urls import patterns, include, url
from rest_framework import routers
from laundry import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('laundry.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
