from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CoffeeUser

# Stuff to have a new user class admin

# class CoffeeUserInline(admin.StackedInline):
#     model = CoffeeUser
#     verbose_name_plural = 'coffeeusers'

# Define a new User admin
class CoffeeUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'ratio_sharing', 'facebook')

# # Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(CoffeeUser, CoffeeUserAdmin)
