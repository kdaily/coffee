from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from .models import Coffee, CoffeeBag, RoastedCoffeeBag
from .models import Roaster, UserRoaster
from .models import Store, UserStore
from .models import CoffeeBagImage

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class CoffeeAdmin(GuardedModelAdmin):
    pass

class UserRoasterAdmin(GuardedModelAdmin):
    pass

class UserStoreAdmin(GuardedModelAdmin):
    pass

admin.site.register(Coffee, CoffeeAdmin)
## admin.site.register(Coffee)

admin.site.register(Roaster)
admin.site.register(UserRoaster, UserRoasterAdmin)
admin.site.register(Store)
admin.site.register(UserStore, UserStoreAdmin)
admin.site.register(CoffeeBag)
admin.site.register(RoastedCoffeeBag)
admin.site.register(CoffeeBagImage)
