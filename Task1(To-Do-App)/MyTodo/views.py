from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def Home_View(request):
    dict = Task.objects.all()
    return render(request,'MyTodo/home.html',{'task':dict})

def Add_Task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        end_date = str(request.POST['end_date'])
        status = request.POST['status']
        priority = request.POST['priority']
        assignees = request.POST['assignees']
        task=Task()
        task.task_name = task_name
        task.end_date = end_date
        task.status = status
        task.priority = priority
        task.assignees = assignees
        task.save()
        return redirect('Home')
    return render(request,'MyTodo/form.html')

def Edit_Task(request,pk):
    task = Task.objects.get(pk=pk)
    return render(request,'MyTodo/edit.html',{'task':task})

def Update_Task(request,pk):
    task = Task.objects.get(pk=pk)
    task.task_name = request.POST['task_name']
    task.end_date = str(request.POST['end_date'])
    task.status = request.POST['status']
    task.priority = request.POST['priority']
    task.assignees = request.POST['assignees']
    task.save()
    return redirect('Home')

def Delete_Task(request,pk):
    obj = Task.objects.get(pk=pk)
    if obj:
        obj.delete()
        return redirect('Home')
    return render(request,'MyTodo/home.html')