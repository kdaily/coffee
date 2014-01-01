from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Preparation, Method
from .models import CoffeeGrinder, PurchasedCoffeeGrinder

class PreparationAdmin(GuardedModelAdmin):
    pass

admin.site.register(Preparation, PreparationAdmin)
admin.site.register(Method)
admin.site.register(CoffeeGrinder)
admin.site.register(PurchasedCoffeeGrinder)
