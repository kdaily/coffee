from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django import forms

from .models import CoffeeUser

# Stuff to have a new user class admin

# class CoffeeUserInline(admin.StackedInline):
#     model = CoffeeUser
#     verbose_name_plural = 'coffeeusers'

class CoffeeUserForm(forms.ModelForm):
    """Form for changing CoffeeUser.

    Currently only used in the admin panel; this could change.

    """

    class Meta:
        model = CoffeeUser

# Define a new User admin
class CoffeeUserAdmin(UserAdmin):

    form = CoffeeUserForm

    # What to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Overloads what to display in the form
    fieldsets = ((None, 
                  {'fields': ('username', 'password')}),

                 ('Personal info',
                   {'fields': ('first_name', 'last_name', 'email', 'skill_level', 'avatar')}),

                 ('Permissions',
                   {'fields': ('is_active',
                               'is_staff',
                               'is_superuser',
                               'groups',
                               'user_permissions')}),

                 ('Important dates',
                   {'fields': ('last_login', 'date_joined')}),

                 ('Social media',
                  {'fields': ('facebook', 'twitter', 'gplus')}),

                 ('Sharing',
                  {'fields': ('purch_coffee_bag_sharing', 'ratio_sharing', 'friends')}))

    # Makes it easier to select many-to-many fields
    filter_horizontal = ('friends', 'groups')

# # Re-register UserAdmin
admin.site.register(CoffeeUser, CoffeeUserAdmin)
    
