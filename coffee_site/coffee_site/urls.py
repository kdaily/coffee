from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coffee_site.views.home', name='home'),
    # url(r'^coffee_site/', include('coffee_site.foo.urls')),

    url(r'^base/$', 'base.views.index'),
    url(r'^base/coffees/$', 'coffee_journal.views.index'),
    url(r'^base/coffee/(?P<coffee_id>\d+)/$', 'coffee_journal.views.coffee_detail'),

    url(r'^coffee_journal/coffees/$', 'coffee_journal.views.index'),
    url(r'^coffee_journal/coffee/(?P<coffee_id>\d+)/$', 'coffee_journal.views.coffee_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

