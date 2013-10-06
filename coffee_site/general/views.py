# Create your views here.
import logging

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext, Context, loader
from django.contrib.auth.models import User
from django.contrib import auth

from braces.views import LoginRequiredMixin

from .models import Coffee, CoffeeBag, CoffeeForm, CoffeeBagForm
from .models import Roaster, UserRoaster
from profile.models import CoffeeUser

from django.utils import simplejson

logger = logging.getLogger('views')

def home(request):
    """Display the home (index) page.
    
    One version is displayed if the user is logged in,
    and another if not.
    
    """

    if request.user.is_authenticated():
        response = render_to_response('index.html', 
                                      context_instance=RequestContext(request))
    else:
        response = render_to_response('index.html',
                                      context_instance=RequestContext(request))
    
    return response

def login_user(request):
    """User login.
    Handles successful/unsuccessful logins.
    This was meant to be specific to the coffee journal portion
    of the app, but probably could be used site-wide (coffee ratio too)
    """

    state = "Please log in below..."
    username = ''
    password = ''
        
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                state = "You're successfully logged in!"

                return render_to_response('coffee_journal/index.html',
                                          {'state': state, 'username': username},
                                          context_instance=RequestContext(request))

                ## return redirect('coffee_bag.views.coffees')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('index.html',
                              {'state': state, 'username': username},
                              context_instance=RequestContext(request))


def logout(request):
    """Log users out and re-direct them to the login page.
    
    """
    
    auth.logout(request)

    return HttpResponseRedirect('/')

    
def roaster_list_view(request, *args, **kwargs):
    """View to get a paginated list of all roasters.
    """
    
    if request.user.is_authenticated():
        user_roaster_list = UserRoaster.objects.filter(user=request.user.id)
        urlist = [uroaster.roaster for uroaster in user_roaster_list]
    
    else:
        urlist = []
    
    return render_to_response('general/roasters.html', 
                              {'roaster_list': Roaster.objects.all(), 
                               'uroaster_list': urlist, 
                               'num_vote_stars': [5,4,3,2,1],
                               'paginate_by': 6},
                              context_instance=RequestContext(request))

    
class RoasterDetailView(DetailView):
    """View to get the detailed view for a roaster.
    """
    
    model = Roaster
    template_name = 'general/roaster_detail.html'
   

class UserRoasterListView(ListView):
    """View to get a paginated list of all roasters.
    """

    def get_queryset(self, *args, **kwargs):
        """Override get_queryset so we can filter on request.user """
        return UserRoaster.objects.filter(user=self.request.user.id)      
    
    template_name = 'general/roasters.html'
    paginate_by = 6
    context_object_name = 'roaster_list'
    
@login_required    
def rate_user_roaster(request, *args, **kwargs):
    json_vars = {}
    
    logger.debug("In rate_user_roaster")
    logger.debug("request POST: %s" % (request.POST, ))
    
    if request.method == 'POST':

        rating = int(request.POST.get('rating', None))
        roaster_pk = request.POST.get('roaster_pk', None)

        curruser = request.user
        roaster = Roaster.objects.get(pk=roaster_pk)

        logger.debug("Trying to update: %s added %i to %s" % (curruser, 
                                                              rating, 
                                                              roaster))

        try:
            roaster.rating.delete(request.user, request.META['REMOTE_ADDR'])
        except Exception as e:
            logger.error("Can't delete: %s" % e)

        try:
            roaster.rating.add(score=rating, user=request.user, 
                               ip_address=request.META['REMOTE_ADDR'])
            roaster.save()
            logger.debug("%s added %i to %s" % (curruser, rating, roaster))
            state = 'success'
        except Exception as e:
            logger.error("%s" % e)
            state = "Already added that roaster"

        json_vars['state'] = state
    
    return HttpResponse(simplejson.dumps(json_vars),
                        mimetype='application/javascript')

@login_required    
def add_user_roaster(request, *args, **kwargs):

    json_vars = {}
    
    if request.method == 'POST':

        state = "add a UserRoaster"
    
        # curruser = request.user
        curruser = CoffeeUser.objects.get(pk=request.user.id)
        roaster = Roaster.objects.get(pk=request.POST.get('roaster_pk', None))
        
        print curruser, roaster
        
        try:
            user_roaster = UserRoaster(user=curruser,
                                       roaster=roaster)
            user_roaster.save()
            state = 'success'
        except:
            state = "Already added that roaster"

        json_vars['state'] = state
    
    return HttpResponse(simplejson.dumps(json_vars),
                        mimetype='application/javascript')
    
    
@login_required    
def remove_user_roaster(request, *args, **kwargs):
    """Remove a user roaster object from the db.
    
    Need to check to make sure a single value is removed.
    
    Also, user shouldn't be able to navigate to this URL directly;
    must be a mechanism to limit this.
    
    """
    
    json_vars = {}
    
    print "I'm here"
    
    if request.method == 'POST':

        state = "remove a UserRoaster"
        
        roaster_pk = request.POST.get('roaster_pk', None)
        
        if roaster_pk:
            try:
                user_roaster = UserRoaster.objects.get(user=request.user.id,
                                                       roaster=roaster_pk)
                user_roaster.delete()
                state = 'success'
            except:
                state = "Already removed that roaster"
            
            json_vars['state'] = state
            
            return HttpResponse(simplejson.dumps(json_vars),
                        mimetype='application/javascript')
        else:
            return redirect("roaster_list_view")
    else:
        return redirect("roaster_list_view")
        
class CoffeeListView(ListView):
    """View to get a paginated list of all coffees.
    """
    
    model = Coffee
    
    template_name = 'coffee_journal/coffee/coffee_list.html'
    paginate_by = 5
    
    context_object_name = 'coffee_list'

class CoffeeBagListView(ListView):
    """View to get a paginated list of all coffee bags.
    """
    
    model = CoffeeBag
    
    template_name = 'coffee_journal/coffee/coffeebag_list.html'
    paginate_by = 5
    
    context_object_name = 'coffeebag_list'

class CoffeeDetailView(DetailView):
    """View to get the detailed view for a coffee.
    """
    
    model = Coffee
    template_name = 'coffee_journal/coffee/coffee_detail.html'

class CoffeeBagDetailView(DetailView):
    """View to get the detailed view for a coffee bag.
    """
    
    model = CoffeeBag
    template_name = 'coffee_journal/coffee/coffeebag_detail.html'

class CoffeeCreateView(LoginRequiredMixin, CreateView):
    """View to create a new coffee.
    Since this can only be done by a logged in user, the user
    is set in the form initially, and that field should be excluded
    from view.
    """

    model = Coffee
    form_class = CoffeeForm
    template_name = 'coffee_journal/coffee/coffee_create.html'

    context_object_name = 'coffee_create'

    def get(self, request, *args, **kwargs):
        """Action to perform when GET method is used.

        Render the form.

        """
        
        curruser = User.objects.get(pk=request.user.id)
        form = self.form_class(initial={'user': curruser})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Action to perform when POST method is used

        Process the form. Validation is currently done by default.
        Probably could use some custom validation though, and possibly
        some validation at the Javascript level (but don't rely on that!)
        
        """
        
        form = CoffeeForm(request.POST)

        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return redirect('coffeedetail', pk=cmodel.pk)
        
        return render(request, self.template_name, {'form': form})
