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

def bootstrap(request):
    t = loader.get_template('base/bootstrap.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def coffees(request):
    latest_coffee_list = Coffee.objects.all()

    t = loader.get_template('coffee_journal/index.html')

    c = RequestContext(request, {'latest_coffee_list': latest_coffee_list, 'user': request.user})

    return HttpResponse(t.render(c))


class RoasterListView(ListView):

    model = Roaster

    template_name = 'base/roaster_list.html'
    paginate_by = 6

    context_object_name = 'roaster_list'

class RoasterDetailView(DetailView):
    model = Roaster
    template_name = 'base/roaster_detail.html'

    
class CoffeeListView(ListView):

    model = Coffee

    template_name = 'base/coffee_list.html'
    paginate_by = 5

    context_object_name = 'coffee_list'

class CoffeeBagListView(ListView):

    model = CoffeeBag

    template_name = 'base/coffeebag_list.html'
    paginate_by = 5

    context_object_name = 'coffeebag_list'

class CoffeeDetailView(DetailView):
    model = Coffee
    template_name = 'base/coffee_detail.html'

class CoffeeBagDetailView(DetailView):
    model = CoffeeBag
    template_name = 'base/coffeebag_detail.html'

class CoffeeCreateView(LoginRequiredMixin, CreateView):
    model = Coffee
    form_class = CoffeeForm
    template_name = 'base/coffee_create.html'

    context_object_name = 'coffee_create'

    def get(self, request, *args, **kwargs):
        curruser = User.objects.get(pk=request.user.id)
        form = self.form_class(initial={'user': curruser})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = CoffeeForm(request.POST)

        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return redirect('coffeedetail', pk=cmodel.pk)
        
        return render(request, self.template_name, {'form': form})

# @login_required
# def coffee_add(request):
#     # sticks in a POST or renders empty form

#     curruser = User.objects.get(pk=request.user.id)

#     if request.method == 'POST':
#         form = CoffeeForm(request.POST)
#         if form.is_valid():
#             cmodel = form.save()
#             #This is where you might chooose to do stuff.
#             #cmodel.name = 'test1'
#             cmodel.save()
#             return redirect('coffee_journal.views.coffee_detail', coffee_id=cmodel.pk)
    
#     else:
#         form = CoffeeForm(initial={'user': curruser})

#     return render_to_response('coffee_journal/coffee_add.html',
#                               {'coffee_form': form},
#                               context_instance=RequestContext(request))
