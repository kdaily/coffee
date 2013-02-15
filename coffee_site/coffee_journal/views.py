from base.models import Coffee
from django.http import HttpResponse

# Create your views here.
def index(request):
    latest_coffee_list = Coffee.objects.all().order_by('-date_purch')[:5]
    output = ', '.join([p.name for p in latest_coffee_list])
    return HttpResponse(output)
