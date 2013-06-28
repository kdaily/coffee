from base.models import Coffee
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from base.models import CoffeeUser

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'finca', 'date_purch', 'date_roast', 'purch_location', 'date_roast', 'amount', 'roaster')


    fieldsets = [
        ('Coffee',               {'fields': ['name', 'finca', 'grower', 'varietal', 'altitude', 'notes']}),
        ('Roaster',               {'fields': ['roaster', 'amount', 'date_roast']}),
        ('Purchase', {'fields': ['date_purch', 'purch_location'], 'classes': ['collapse']})
        ]

class CoffeeUserInline(admin.StackedInline):
    model = CoffeeUser
    can_delete = False
    verbose_name_plural = 'coffeeusers'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (CoffeeUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Coffee, CoffeeAdmin)
