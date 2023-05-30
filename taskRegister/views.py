from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TaskForm
from .models import TaskList
# Create your views here.
def testing(request):
    return render(request, 'taskRegister/home.html')  

def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['task_name']
            ds = form.cleaned_data['task_description']
            t = TaskList(name=nm, description=ds, status=True)
            t.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request, 'taskRegister/addTask.html', {'form' : form})