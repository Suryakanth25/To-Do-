from django.shortcuts import render, get_object_or_404, redirect
from  django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    tasks = Todo.objects.order_by('created_at')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()

    return render(request, 'Base/index.html', {'form':form, 'tasks':tasks})


def delete(request, id):
    task = get_object_or_404(Todo, id=id)
    task.delete()
    return redirect('todo')