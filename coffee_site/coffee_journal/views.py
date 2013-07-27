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

from base.models import Coffee, CoffeeBag, CoffeeForm, CoffeeBagForm
from .models import PurchasedCoffeeBag, PurchasedCoffeeBagForm

# Create your views here.

def login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect("/coffees/")
                ## return redirect('coffee_journal.views.coffees')

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('coffee_journal/login.html',
                              {'state':state, 'username': username},
                              context_instance=RequestContext(request))

@login_required
def home(request):
    return render_to_response('coffee_journal/index.html',
                              context_instance=RequestContext(request))

# @login_required
# def coffee_carousel(request):
#     return render_to_response('coffee_journal/coffee_carousel.html',
#                               context_instance=RequestContext(request))

def logout(request):
    """
    Log users out and re-direct them to the main page.
    """
    auth.logout(request)

    # return HttpResponseRedirect('/login/')
    return redirect('coffee_journal.views.login')

class PurchasedCoffeeBagDetailView(DetailView):
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_detail.html'

class PurchasedCoffeeBagCreateView(LoginRequiredMixin, CreateView):
    model = PurchasedCoffeeBag
    form_class = PurchasedCoffeeBagForm

    template_name = 'coffee_journal/purchasedcoffeebag_create.html'

    context_object_name = 'purch_coffee_create'

    def get(self, request, *args, **kwargs):
        curruser = User.objects.get(pk=request.user.id)
        form = self.form_class(initial={'id_user': curruser})
        ## form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return redirect('purchcoffeebagdetail', pk=cmodel.pk)
        
        return render(request, self.template_name, {'form': form})


class PurchasedCoffeeBagListView(ListView):

    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 5 
    context_object_name = 'purchasedcoffeebag_list'

class UserPurchasedCoffeeBagListView(ListView):

    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 5

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.args[0])
        return PurchasedCoffeeBag.objects.filter(user__id=self.user.id).order_by('-date_purch')

class SearchPurchasedCoffeeBagListView(ListView):

    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(SearchPurchasedCoffeeBagListView, self).get_queryset()
        
        q = self.request.GET.get("q")
        return queryset.filter(varietal__icontains=q)
    
# @login_required
# def purchased_coffees_paginated(request):
#     latest_coffee_list = PurchasedCoffeeBag.objects.filter(user__id=request.user.id).order_by('-date_purch')
#     paginator = Paginator(latest_coffee_list, 5)

#     t = loader.get_template('coffee_journal/purchased_coffees_paginated.html')

#     page = request.GET.get('page')
    
#     try:
#         coffees = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         coffees = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         coffees = paginator.page(paginator.num_pages)

#     c = RequestContext(request, {'latest_coffee_list': coffees, 'user': request.user})
#     return HttpResponse(t.render(c))

class CoffeeDetailView(DetailView):
    model = Coffee
    template_name = 'base/coffee_detail.html'

class CoffeeBagDetailView(DetailView):
    model = CoffeeBag
    template_name = 'base/coffeebag_detail.html'

class PurchasedCoffeeBagDetailView(DetailView):
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_detail.html'

# def purchased_coffee_detail(request, coffee_id):
#     coffee = PurchasedCoffeeBag.objects.get(pk=coffee_id)

#     t = loader.get_template('coffee_journal/purchased_coffee_detail.html')
#     c = RequestContext(request, {'coffee': coffee})

#     return HttpResponse(t.render(c))

