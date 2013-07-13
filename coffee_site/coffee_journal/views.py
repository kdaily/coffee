from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from base.models import Coffee, CoffeeBag, PurchasedCoffeeBag
from base.models import CoffeeForm, CoffeeBagForm, PurchasedCoffeeBagForm

from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def coffees(request):
    latest_coffee_list = Coffee.objects.all()

    t = loader.get_template('coffee_journal/index.html')

    c = RequestContext(request, {'latest_coffee_list': latest_coffee_list, 'user': request.user})

    return HttpResponse(t.render(c))

def coffees_paginated(request):
    latest_coffee_list = Coffee.objects.all()
    paginator = Paginator(latest_coffee_list, 5)

    t = loader.get_template('coffee_journal/coffees_paginated.html')

    page = request.GET.get('page')
    
    try:
        coffees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        coffees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        coffees = paginator.page(paginator.num_pages)

    c = RequestContext(request, {'latest_coffee_list': coffees, 'user': request.user})
    
    return HttpResponse(t.render(c))

@login_required
def purchased_coffees_paginated(request):
    latest_coffee_list = PurchasedCoffeeBag.objects.filter(user__id=request.user.id).order_by('-date_purch')
    paginator = Paginator(latest_coffee_list, 5)

    t = loader.get_template('coffee_journal/coffees_paginated.html')

    page = request.GET.get('page')
    
    try:
        coffees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        coffees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        coffees = paginator.page(paginator.num_pages)

    c = RequestContext(request, {'latest_coffee_list': coffees, 'user': request.user})
    
    return HttpResponse(t.render(c))

def coffee_detail(request, coffee_id):
    coffee = Coffee.objects.get(pk=coffee_id)

    t = loader.get_template('coffee_journal/coffee_detail.html')
    c = RequestContext(request, {'coffee': coffee})

    return HttpResponse(t.render(c))

def purchased_coffee_detail(request, coffee_id):
    coffee = PurchasedCoffeeBag.objects.get(pk=coffee_id)

    t = loader.get_template('coffee_journal/purchased_coffee_detail.html')
    c = RequestContext(request, {'coffee': coffee})

    return HttpResponse(t.render(c))

@login_required
def coffee_add(request):
    # sticks in a POST or renders empty form

    curruser = User.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return redirect('coffee_journal.views.coffee_detail', coffee_id=cmodel.pk)
    
    else:
        form = CoffeeForm(initial={'user': curruser})

    return render_to_response('coffee_journal/coffee_add.html',
                              {'coffee_form': form},
                              context_instance=RequestContext(request))

def add_coffee(request):
    pass
