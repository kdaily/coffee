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



class PurchasedCoffeeBagDetailView(DetailView):
    """Detail view for purchased coffee bags.
    
    """
    
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_detail.html'



class PurchasedCoffeeBagListView(ListView):
    """View for a list of purchased coffee bags.
        
    """
    
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 8 
    context_object_name = 'purchasedcoffeebag_list'

class UserPurchasedCoffeeBagListView(LoginRequiredMixin, ListView):
    """View a paginated list of purchased coffee bags for the logged in user.
    
    """
    
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 5

    def get_queryset(self):
        """Get list of purchased coffee bags from the DB for the currently logged in user.
        
        """
        
        # Get the current user, or return a 404 error
        self.user = get_object_or_404(User, username=self.args[0])
        
        return PurchasedCoffeeBag.objects.filter(user__id=self.user.id).order_by('-date_purch')

class SearchPurchasedCoffeeBagListView(ListView):
    """Testing example - search the purchased coffee bags for keyword in varietal column.
    
    This is a bad and slow way to implement searching; needs a dedicated indexed search functionality.
    There are many Django packages that provide this.
    
    """
    
    model = PurchasedCoffeeBag
    template_name = 'coffee_journal/purchasedcoffeebag_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        """Override the queryset to search for keyword in varietal column.
        
        """
        
        # Default way to get the query set
        queryset = super(SearchPurchasedCoffeeBagListView, self).get_queryset()
        
        # Get the query filter parameters
        # Currently only searches the varietal label
        q = self.request.GET.get("q")
        
        return queryset.filter(varietal__icontains=q)
    
class PurchasedCoffeeBagCreateView(LoginRequiredMixin, CreateView):
    """View to add new purchased coffee bags.
    
    """

    model = PurchasedCoffeeBag
    form_class = PurchasedCoffeeBagForm

    template_name = 'coffee_journal/purchasedcoffeebag_create.html'

    context_object_name = 'purch_coffee_create'

    def get(self, request, *args, **kwargs):
        """Handle GET requests.
        
        Display the form; initializes the user variable to the currently logged
        in user.
        
        """
        
        curruser = User.objects.get(pk=request.user.id)
        form = self.form_class(initial={'id_user': curruser})
        
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Handle POST requests.
        
        Process the form. Currently uses default validation, could probably
        use some custom validation.
        
        """
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return redirect('purchcoffeebagdetail', pk=cmodel.pk)
        
        return render(request, self.template_name, {'form': form})
