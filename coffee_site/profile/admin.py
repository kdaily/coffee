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

    class Meta:
        model = CoffeeUser

# Define a new User admin
class CoffeeUserAdmin(UserAdmin):

    form = CoffeeUserForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'ratio_sharing')

    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Personal info',
                   {'fields': ('first_name', 'last_name', 'email', 'skill_level',)}),
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

    filter_horizontal = ('friends', 'groups')

# # Re-register UserAdmin
admin.site.register(CoffeeUser, CoffeeUserAdmin)
    
