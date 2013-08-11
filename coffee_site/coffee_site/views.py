from django.template import RequestContext, Context, loader
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from braces.views import LoginRequiredMixin

from coffee_site_general.models import Coffee, CoffeeBag, CoffeeForm, CoffeeBagForm
from coffee_bag.models import PurchasedCoffeeBag, PurchasedCoffeeBagForm

# Create your views here.


def home(request):
    """Display the home (index) page.
    
    Shouldn't need a login required, and needs to handle when
    users are not logged in.
    
    """
    
    return render_to_response('index.html',
                              context_instance=RequestContext(request))
    
def login(request):
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
                return HttpResponseRedirect("/coffees/")
                ## return redirect('coffee_bag.views.coffees')

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('coffee_journal/login.html',
                              {'state': state, 'username': username},
                              context_instance=RequestContext(request))
        

def logout(request):
    """Log users out and re-direct them to the login page.
    
    """
    
    auth.logout(request)

    return redirect('coffee_bag.views.login')

