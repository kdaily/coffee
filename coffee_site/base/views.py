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

from braces.views import LoginRequiredMixin

from .models import Coffee, CoffeeBag, CoffeeForm, CoffeeBagForm
from .models import Roaster

def logout_view(request):
    logout(request)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", 
                  {'form': form,})

class RoasterListView(ListView):
    """View to get a paginated list of all roasters.
    
    """
    
    model = Roaster
    
    template_name = 'base/roaster_list.html'
    paginate_by = 6
    
    context_object_name = 'roaster_list'

class RoasterDetailView(DetailView):
    """View to get the detailed view for a roaster.
        
    """
    
    model = Roaster
    template_name = 'base/roaster_detail.html'

class CoffeeListView(ListView):
    """View to get a paginated list of all coffees.
    
    """
    
    model = Coffee
    
    template_name = 'base/coffee_list.html'
    paginate_by = 5
    
    context_object_name = 'coffee_list'

class CoffeeBagListView(ListView):
    """View to get a paginated list of all coffee bags.
    
    """
    
    model = CoffeeBag
    
    template_name = 'base/coffeebag_list.html'
    paginate_by = 5
    
    context_object_name = 'coffeebag_list'

class CoffeeDetailView(DetailView):
    """View to get the detailed view for a coffee.
        
    """
    
    model = Coffee
    template_name = 'base/coffee_detail.html'

class CoffeeBagDetailView(DetailView):
    """View to get the detailed view for a coffee bag.
        
    """
    
    model = CoffeeBag
    template_name = 'base/coffeebag_detail.html'

class CoffeeCreateView(LoginRequiredMixin, CreateView):
    """View to create a new coffee.
    
    Since this can only be done by a logged in user, the user
    is set in the form initially, and that field should be excluded
    from view.
        
    """

    model = Coffee
    form_class = CoffeeForm
    template_name = 'base/coffee_create.html'

    context_object_name = 'coffee_create'

    def get(self, request, *args, **kwargs):
        """Action to perform when GET method is used
        
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
