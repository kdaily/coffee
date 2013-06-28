# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse("Hello, world. You're at the base index.")


def logout_view(request):
    logout(request)


