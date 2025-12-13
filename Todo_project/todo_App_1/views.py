from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_App_1.models import todo_App_1
# Create your views here.

def hello(request):
    todo = todo_App_1.objects.last()
    html = f"""
    <h1>Hello World</h1>
    <p>This is html Response</p>
    <p>Todo Title : {todo.title} </p>
    """
    return HttpResponse(html)

def index(request):
    todo = todo_App_1.objects.first()

    a = {
        'title': todo.title,
        'description': "This is json response"
    }
    return JsonResponse(a)

def bye(request):
    todos = todo_App_1.objects.all()
    show=True
    page_name = "temp.html"
    my_dict = {'todos' : todos, 'show': show}
    return render(request, page_name, context= my_dict)
