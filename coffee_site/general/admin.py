from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from .models import Coffee, CoffeeBag, Roaster, Store

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class CoffeeAdmin(GuardedModelAdmin):
    pass

admin.site.register(Coffee, CoffeeAdmin)
## admin.site.register(Coffee)

admin.site.register(Roaster)
admin.site.register(UserRoaster)
admin.site.register(Store)
admin.site.register(UserStore)
admin.site.register(CoffeeBag)
admin.site.register(RoastedCoffeeBag)
