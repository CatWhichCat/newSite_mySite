from django.shortcuts import render
from .models import *


def index(request):
    task = Task.objects.all()
    
    return render(request, 'main/index.html', {'title': 'Главаня страница', 'Task': task})
    
    
def about(request):
    return render(request, 'main/about.html')

def create(request):
    return render(request, 'main/create_task.html')