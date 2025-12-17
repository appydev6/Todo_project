from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todo_App_1.models import todo_App_1
# Create your views here.

def index(request):
    all_todos = todo_App_1.objects.all().order_by('id')
    data = {
        "todos" : all_todos
    }
    page_name = "index.html"
    return render(request, page_name, context=data)

def add_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid method")
    else:
        todo_input= request.POST['todoInput']
        todo_Object= todo_App_1.objects.create(title=todo_input)
        # return redirect(f'/todos_app_1?new_id={todo_Object.id}')
        return redirect('todo_index')

def delete_view(request, todo_id):
    if request.method == "POST":
        return HttpResponse("Invalid method")
    else:
        try:
            todo_object= todo_App_1.objects.get(id=todo_id)
            todo_object.delete()
            return redirect('todo_index')
        except todo_object.DoesNotExist:
            return HttpResponse("Error Todo Not Found")

def mark_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid method")
    else:
        try:
            todo_id = request.POST['todo_id']
            todo_object = todo_App_1.objects.get(id=todo_id)
            todo_object.completed = True
            todo_object.save()
            return redirect('todo_index')
        except todo_App_1.DoesNotExist:
            return HttpResponse("Error Todo Not Found")
