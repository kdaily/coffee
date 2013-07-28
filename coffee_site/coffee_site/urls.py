from django.conf.urls import patterns, include, url
from django.contrib.auth import logout

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coffee_journal.views import PurchasedCoffeeBagDetailView
from coffee_journal.views import PurchasedCoffeeBagListView
from coffee_journal.views import UserPurchasedCoffeeBagListView
from coffee_journal.views import PurchasedCoffeeBagCreateView
from base.views import CoffeeListView, CoffeeCreateView, CoffeeDetailView
from base.views import CoffeeBagListView, CoffeeBagDetailView
from base.views import RoasterListView, RoasterDetailView

urlpatterns = patterns('',
                       # Examples:
                           
                       
                       # url(r'^login/$', 'django.contrib.auth.views.login'),                       
                       ## url(r'^logout/$', 'django.contrib.auth.views.logout'),                       
                                              
                       url(r'^$', 'coffee_journal.views.home', name='home'),

                       url(r'^register/$', 'base.views.register'),                       
                       url(r'^login/$', 'coffee_journal.views.login'),                       
                       url(r'^logout/$', 'coffee_journal.views.logout'),

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

                       url(r'^purchased_coffees/([A-Za-z]+[\w-]*)/$', 
                           view=UserPurchasedCoffeeBagListView.as_view(),
                           name="userpurchcoffeebaglist"),

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

                       url(r'^roasters/$', 
                           view=RoasterListView.as_view(),
                           name="roasterlist"),

                       url(r'^roaster/(?P<pk>\d+)/$', 
                           view=RoasterDetailView.as_view(),
                           name="roasterdetail"),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Only for devel!!!
                       # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
                       
                       )

