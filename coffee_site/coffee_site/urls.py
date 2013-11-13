from django.conf.urls import patterns, include, url
from django.contrib.auth import logout

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coffee_bag.views import PurchasedCoffeeBagDetailView
from coffee_bag.views import PurchasedCoffeeBagListView
from coffee_bag.views import UserPurchasedCoffeeBagListView
from general.views import CoffeeListView, CoffeeCreateView, CoffeeDetailView
from general.views import CoffeeBagListView, CoffeeBagDetailView
from general.views import roaster_list_view, RoasterDetailView, UserRoasterListView


media_root = getattr(settings, 'MEDIA_ROOT', '/media')    


urlpatterns = patterns('',
                       # Examples:
                           
                       #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       #url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
                       #url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
                       #url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
                       #url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
                       #url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
                       #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
                       #url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),  
                       
                       # Main page
                       url(r'^$', 'general.views.home', name='home'),
                       
                       # Main page when logged in
                       url(r'login/$', 'general.views.login_user'),
                       url(r'logout/$', 'general.views.logout'),
                       
                       url('^register/$', CreateView.as_view(template_name='signup.html', form_class=UserCreationForm, success_url='/')),
                       
                       url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': media_root}),
                       
                       # View a list of roasters
                       url(r'^roasters/$', 
                           'general.views.roaster_list_view', 
                           name="roaster_list_view"),

                       # View a list of roasters
                       url(r'^coffeebag_by_roaster_json/$', 
                           'general.views.coffeebag_by_roaster_view_json', 
                           name="coffeebag_by_roaster_view_json"),
                       
                       # View details for roaster by primary key
                       url(r'^roaster/(?P<pk>\d+)/$', 
                           view=RoasterDetailView.as_view(),
                           name="roasterdetail"),
                       
                       # View a list of roasters for a user
                       url(r'^myroasters/$', 
                           login_required(UserRoasterListView.as_view()),
                           name="myroasterlist"),
                       
                       # Add a roaster to current user's roaster list                     
                       url(r'^adduserroaster/$', 
                           view='general.views.add_user_roaster',
                           name="add_user_roaster"),
                       
                       # Remove a roaster to current user's roaster list                     
                       url(r'^removeuserroaster/$', 
                           view='general.views.remove_user_roaster',
                           name="remove_user_roaster"),

                       # Remove a roaster to current user's roaster list                     
                       url(r'^rateuserroaster/$', 
                           view='general.views.rate_user_roaster',
                           name="rate_user_roaster"),

                                              
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
                           view='coffee_bag.views.purchased_coffee_bag_create_view',
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

                      
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Only for devel!!!
                       # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
                       
                       )

