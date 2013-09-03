from django.contrib import admin

from .models import PurchasedCoffeeBag

class PurchasedCoffeeBagAdmin(GuardedModelAdmin):
    pass

admin.site.register(PurchasedCoffeeBag, PurchasedCoffeeBagAdmin)
