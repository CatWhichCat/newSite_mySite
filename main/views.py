from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    task = Task.objects.all()
    
    return render(request, 'main/index.html', {'title': 'Главаня страница', 'Task': task})
    
    
def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    
    form = TaskForm()
    context = {
        'form': form
    }
    
    return render(request, 'main/create_task.html', context)