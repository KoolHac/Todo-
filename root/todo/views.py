from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import *
from .models import *


@login_required(login_url='/accounts/login')
def main_view(request):
    form = TaskForm()
    task = Task.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('/todo/')
        else:
            return HttpResponse("Error")
    else:
        return render(request, 'todo/index.html', {'form': form, 'task': task, 'request': request})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = UpdateForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/todo/')
    else:
        form = UpdateForm(instance=task)
        return render(request, 'todo/update.html', {'form': form, 'task': task})

@login_required(login_url='/accounts/login/')
def home_page(request):
    task = Task.objects.filter(owner=request.user)[:5]
    return render(request, 'todo/home.html', {'request': request, 'task': task})

def delete_task(requst, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('/todo/')

def pending_task(request):
    task = Task.objects.filter(owner=request.user)
    return render(request,'todo/pending.html', {'task': task})

def complete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.complete = True
    if task.complete:
        return redirect('/todo/')
    else:
        return HttpResponse("An error occurred")
