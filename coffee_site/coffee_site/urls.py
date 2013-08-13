from django.conf.urls import patterns, include, url
from django.contrib.auth import logout

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coffee_bag.views import PurchasedCoffeeBagDetailView
from coffee_bag.views import PurchasedCoffeeBagListView
from coffee_bag.views import UserPurchasedCoffeeBagListView
from coffee_bag.views import PurchasedCoffeeBagCreateView
from general.views import CoffeeListView, CoffeeCreateView, CoffeeDetailView
from general.views import CoffeeBagListView, CoffeeBagDetailView
from general.views import RoasterListView, RoasterDetailView

urlpatterns = patterns('',
                       # Examples:
                           
                       
                       # url(r'^login/$', 'django.contrib.auth.views.login'),                       
                       ## url(r'^logout/$', 'django.contrib.auth.views.logout'),                       
                       
                       # Main page
                       url(r'^$', 'coffee_site.views.home', name='home'),

                       # Register/login/logout of the coffee jounal
                       # Probably could all be moved to base.
                       url(r'^login/$', 'coffee_site.views.login'),                       
                       url(r'^logout/$', 'coffee_site.views.logout'),

                       # View detail for a coffee
                       url(r'^coffee/(?P<pk>\d+)/$', 
                           view=CoffeeDetailView.as_view(),
                           name="coffeedetail"),

                       # View detail for a coffee bag
                       url(r'^coffeebag/(?P<pk>\d+)/$', 
                           view=CoffeeBagDetailView.as_view(),
                           name="coffeebagdetail"),

                       # View detail for a purchased coffee bag
                       url(r'^purchcoffeebag/(?P<pk>\d+)/$', 
                           view=PurchasedCoffeeBagDetailView.as_view(),
                           name="purchcoffeebagdetail"),

                       # View list of purchased coffee bags
                       url(r'^purchased_coffees/$', 
                           view=PurchasedCoffeeBagListView.as_view(),
                           name="purchcoffeebaglist"),

                       # View list of purchased coffee bags for a particular user
                       url(r'^purchased_coffees/([A-Za-z]+[\w-]*)/$', 
                           view=UserPurchasedCoffeeBagListView.as_view(),
                           name="userpurchcoffeebaglist"),

                       # Create a new purchased coffee bags
                       url(r'^addpurchcoffeebag/$', 
                           view=PurchasedCoffeeBagCreateView.as_view(),
                           name="purchcoffeebagcreate"),

                       # Create a new coffee 
                       url(r'^addcoffee/$', 
                           view=CoffeeCreateView.as_view(),
                           name="coffeecreate"),

                       # View a list of coffees
                       url(r'^coffees/$', 
                           view=CoffeeListView.as_view(),
                           name="coffeelist"),

                       # View a list of coffee bags
                       url(r'^coffeebags/$', 
                           view=CoffeeBagListView.as_view(),
                           name="coffeebaglist"),

                       # View a list of roasters
                       url(r'^roasters/$', 
                           view=RoasterListView.as_view(),
                           name="roasterlist"),

                       # View details for roaster by primary key
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

