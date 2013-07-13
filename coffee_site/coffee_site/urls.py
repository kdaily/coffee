from django.conf.urls import patterns, include, url
from django.contrib.auth import logout

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                           
                       # url(r'^$', 'coffee_site.views.home', name='home'),
                       # url(r'^coffee_site/', include('coffee_site.foo.urls')),
                       
                       # url(r'^login/$', 'django.contrib.auth.views.login'),                       
                       ## url(r'^logout/$', 'django.contrib.auth.views.logout'),                       
                       
                       # url(r'^login/$', 'coffee_journal.views.login'),
                       ## url(r'^logout/$', 'coffee_journal.views.logout'),
                       
                       url(r'^$', 'coffee_journal.views.home', name='home'),

                       url(r'^register/$', 'base.views.register'),                       
                       url(r'^login/$', 'coffee_journal.views.login'),                       
                       url(r'^logout/$', 'coffee_journal.views.logout'),

                       url(r'^coffees/$', 'coffee_journal.views.coffees_paginated'),
                       url(r'^carousel/$', 'coffee_journal.views.coffee_carousel'),
                       url(r'^coffee/(?P<coffee_id>\d+)/$', 'coffee_journal.views.coffee_detail'),
                       url(r'^add/$', 'coffee_journal.views.coffee_add'),
                       
                       # url(r'^coffee_journal/login/$', 'coffee_journal.views.login'),                       
                       # url(r'^coffee_journal/logout/$', 'coffee_journal.views.logout'),
                       # url(r'^coffee_journal/coffees/$', 'coffee_journal.views.coffees'),
                       # url(r'^coffee_journal/coffee/(?P<coffee_id>\d+)/$', 'coffee_journal.views.coffee_detail'),
                       # url(r'^coffee_journal/add/$', 'coffee_journal.views.coffee_add'),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Only for devel!!!
                       # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
                       
                       )

