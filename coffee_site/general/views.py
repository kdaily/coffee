# Create your views here.
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
from .models import Roaster


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

    
class RoasterListView(ListView):
    """View to get a paginated list of all roasters.
    """
    
    model = Roaster
    
    template_name = 'general/roasters.html'
    paginate_by = 6
    
    context_object_name = 'roaster_list'

class RoasterDetailView(DetailView):
    """View to get the detailed view for a roaster.
    """
    
    model = Roaster
    template_name = 'general/roaster_detail.html'

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
