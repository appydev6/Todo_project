from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todo_App_1.models import todo_App_1
# Create your views here.
COMPLETED_TO_BOOL = {
    "0" : False,
    "1" : True
}

ORDER_TO_STRING = {
    "0" : "created_at",
    "1" : "-created_at"
}

def index(request):
    search = request.GET.get("todoSearch")  #   "request.GET" is itself a dictionary.
    completed = request.GET.get("completed")
    order = request.GET.get("order")
    all_todos = todo_App_1.objects.all()
    if search != None:
        all_todos = all_todos.filter(title__icontains=search)
    if completed!=None:
        value = COMPLETED_TO_BOOL.get(completed)
        all_todos = all_todos.filter(completed=value)
    if order != None:
        value = ORDER_TO_STRING.get(order)
        all_todos = all_todos.order_by(value)

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
