from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def index(request):
    return HttpResponse("<h1>Index</h1>")

def bye(request):
    return HttpResponse("<h1>Bye</h1>")
    