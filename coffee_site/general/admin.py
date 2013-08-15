from general.models import Coffee, CoffeeBag, Roaster, Store
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

from guardian.admin import GuardedModelAdmin

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class CoffeeAdmin(GuardedModelAdmin):
    pass

admin.site.register(Coffee, CoffeeAdmin)
## admin.site.register(Coffee)

admin.site.register(Roaster)
admin.site.register(Store)
admin.site.register(CoffeeBag)


# Stuff to have a new user class admin
# Not using the new user class now...

# class CoffeeUserInline(admin.StackedInline):
#     model = CoffeeUser
#     can_delete = False
#     verbose_name_plural = 'coffeeusers'

# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (CoffeeUserInline, )

# # # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
