from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_App_1.models import todo_App_1
# Create your views here.

def index(request):
    all_todos = todo_App_1.objects.all()
    data = {
        "todos" : all_todos
    }
    page_name = "index.html"
    return render(request, page_name, context=data)


