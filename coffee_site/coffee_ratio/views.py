import logging

from django.template import RequestContext, Context, loader
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from braces.views import LoginRequiredMixin

from .models import Preparation
from .forms import PreparationForm

# Create your views here.

logger = logging.getLogger('views')

class PreparationDetailView(DetailView):
    """Detail view for preparation.
    
    """
    
    model = Preparation
    template_name = 'coffee_ratio/preparation_detail.html'

class PreparationListView(ListView):
    """View for a list of preparations.
        
    """
    
    model = Preparation
    template_name = 'coffee_ratio/preparation_list.html'
    paginate_by = 8
    context_object_name = 'preparation_list'

class MyPreparationListView(LoginRequiredMixin, PreparationListView):
    """View list of preparations for current user.
    """

    def get_queryset(self):
        return Preparation.objects.filter(user=self.request.user)

@login_required
def preparation_create_view(request):
    """View to add new preparations.
    
    """

    if request.user.is_authenticated():

        if request.method == "POST":
            logger.debug("coffee bag = %s" % request.POST.get('coffeebag'))
            logger.debug("roaster = %s" % request.POST.get('roaster'))
            logger.debug("user = %s" % request.POST.get('user'))
        
            form = PreparationForm(request.POST)
            
            if form.is_valid():
                new_prep = form.save(commit=False)
                new_prep.save()
                logger.debug("After first save, user = %s" % new_prep.user)
                new_prep.user.add(request.user)
                new_prep.save()

                return HttpResponseRedirect('/preparations/')

        else:
            form = PreparationForm(initial={'id_user': request.user})
            render_dict = {'form': form}
    
        return render_to_response('coffee_ratio/preparation_create.html',
                                  render_dict,
                                  context_instance=RequestContext(request))

    else:
        response = render_to_response('index.html',
                                      context_instance=RequestContext(request))
