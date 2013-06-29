from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from base.models import Coffee
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect("/coffee_journal/coffees/")

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('coffee_journal/login.html',
                              {'state':state, 'username': username},
                              context_instance=RequestContext(request))

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             c = RequestContext(request, {'login_status': 'Success!'})
#             # Redirect to a success page.
#         else:
#             c = RequestContext(request, {'login_status': 'Failed!'})
#             # Return a 'disabled account' error message
#     else:
#         c = RequestContext(request, {'login_status': 'Invalid Login!'})
    
#     return HttpResponse(t.render(c))

@login_required
def index(request):
    latest_coffee_list = Coffee.objects.filter(user__id=request.user.id).order_by('-date_purch')
    ## latest_coffee_list = Coffee.objects.all().order_by('-date_purch')
    output = ', '.join([p.name for p in latest_coffee_list])

    t = loader.get_template('coffee_journal/index.html')

    c = RequestContext(request, {'latest_coffee_list': latest_coffee_list})

    return HttpResponse(t.render(c))

def coffee_detail(request, coffee_id):
    coffee = Coffee.objects.get(pk=coffee_id)

    t = loader.get_template('coffee_journal/coffee_detail.html')
    c = RequestContext(request, {'coffee': coffee})

    return HttpResponse(t.render(c))
