from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def greet(request, name):
    print(request)
    return HttpResponse(f"Hello {name}")