from base.models import Coffee
from django.contrib import admin

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'finca', 'date_purch', 'date_roast', 'purch_location', 'date_roast', 'amount', 'roaster')


    fieldsets = [
        ('Coffee',               {'fields': ['name', 'finca', 'grower', 'varietal', 'altitude', 'notes']}),
        ('Roaster',               {'fields': ['roaster', 'amount']}),
        ('Purchase', {'fields': ['date_purch', 'purch_location'], 'classes': ['collapse']})
        ]

admin.site.register(Coffee, CoffeeAdmin)
