from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, get_object_or_404

from base.models import Coffee
from django.http import HttpResponse

# Create your views here.
def index(request):
    latest_coffee_list = Coffee.objects.all().order_by('-date_purch')
    output = ', '.join([p.name for p in latest_coffee_list])

    t = loader.get_template('coffee_journal/index.html')

    c = RequestContext(request, {'latest_coffee_list': latest_coffee_list})

    return HttpResponse(t.render(c))

def coffee_detail(request, coffee_id):
    coffee = Coffee.objects.get(pk=coffee_id)

    t = loader.get_template('coffee_journal/coffee_detail.html')
    c = RequestContext(request, {'coffee': coffee})

    return HttpResponse(t.render(c))
