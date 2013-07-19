from django.conf.urls import patterns, include, url
from django.contrib.auth import logout

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coffee_journal.views import PurchasedCoffeeBagDetailView
from coffee_journal.views import PurchasedCoffeeBagListView
from coffee_journal.views import PurchasedCoffeeBagCreateView
from base.views import CoffeeListView, CoffeeCreateView, CoffeeDetailView
from base.views import CoffeeBagListView, CoffeeBagDetailView

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

                       # url(r'^coffees/$', 'base.views.coffees_paginated'),

                       # url(r'^carousel/$', 'coffee_journal.views.coffee_carousel'),

                       url(r'^coffee/(?P<pk>\d+)/$', 
                           view=CoffeeDetailView.as_view(),
                           name="coffeedetail"),

                       url(r'^coffeebag/(?P<pk>\d+)/$', 
                           view=CoffeeBagDetailView.as_view(),
                           name="coffeebagdetail"),

                       url(r'^purchcoffeebag/(?P<pk>\d+)/$', 
                           view=PurchasedCoffeeBagDetailView.as_view(),
                           name="purchcoffeebagdetail"),

                       url(r'^purchased_coffees/$', 
                           view=PurchasedCoffeeBagListView.as_view(),
                           name="purchcoffeebaglist"),

                       url(r'^addpurchcoffeebag/$', 
                           view=PurchasedCoffeeBagCreateView.as_view(),
                           name="purchcoffeebagcreate"),

                       url(r'^addcoffee/$', 
                           view=CoffeeCreateView.as_view(),
                           name="coffeecreate"),

                       url(r'^coffees/$', 
                           view=CoffeeListView.as_view(),
                           name="coffeelist"),

                       url(r'^coffeebags/$', 
                           view=CoffeeBagListView.as_view(),
                           name="coffeebaglist"),

                       url(r'^add/$', 'base.views.coffee_add'),
                       
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

