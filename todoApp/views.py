from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import todo
from . import views
# Create your views here.
def index(request):
    todolist = todo.objects.all()

    if request.method=="POST":
        title = request.POST['title']
        new_todo = todo(title=title)
        new_todo.save()
        return redirect('todo-home')
    return render(request,'index.html',{'todo':todolist})

def delete(request,pk):
    todoitem = todo.objects.get(id=pk)
    todo.delete(todoitem)
    return redirect('todo-home')