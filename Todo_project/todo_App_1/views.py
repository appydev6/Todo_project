from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def hello(request):
    html = """
    <h1>Hello World</h1>
    <h2>This is html Response</h2>
    """
    return HttpResponse(html)

def index(request):
    a = {
        'title': "Hey there",
        'description': "This is json response"
    }
    return JsonResponse(a)

def bye(request):
    page_name = "temp.html"
    return render(request, page_name)
    