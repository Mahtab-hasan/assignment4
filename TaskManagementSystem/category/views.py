from django.shortcuts import render, redirect,get_object_or_404
from .models import TaskCategory as Category
from .forms import TaskCategoryForm

def add_category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskCategoryForm()
    categories = Category.objects.all()
    return render(request, 'category/add_category.html', {'form': form,  'categories': categories})
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        category.delete()
        return redirect('add_category')
    return render(request, 'category/delete_category.html', {'category': category})
