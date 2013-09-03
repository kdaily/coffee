from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import PurchasedCoffeeBag

class PurchasedCoffeeBagAdmin(GuardedModelAdmin):
    pass

admin.site.register(PurchasedCoffeeBag, PurchasedCoffeeBagAdmin)
