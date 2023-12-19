from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
from.forms import TaskForm
from category.models import  TaskCategory

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request,'task/show_tasks.html', {'tasks':tasks})

def add_task(request):
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            selected_category_id = request.POST.get('category')
            if selected_category_id:
                form.instance.category_id = selected_category_id
                print(form.instance.category_id)
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    categories = TaskCategory.objects.all()
    return render(request,'task/add_task.html', {'form':form, 'categories':categories})

def edit_task(request,id):
    task = get_object_or_404(Task,pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html',{'form': form})

def delete_task(request,id):
    task = get_object_or_404(Task,pk=id)
    if request.method =='POST':
        task.delete()
        return redirect('show_tasks')
    else:
        return render(request,'task/delete.html',{'task':task})