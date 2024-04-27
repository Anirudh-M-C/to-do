from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='login')
def index(request):
    data=Task.objects.all()
    if 'search_bar' in request.GET:
        search_bar=request.GET['search_bar']
        # data=Data.objects.filter(first_name__icontains=search_bar)
        data=Task.objects.filter(Q(title__icontains=search_bar) | Q(project__icontains=search_bar))

    # Sorting based on query parameters
    sort_by = request.GET.get('sort_by', None)
    if sort_by:
        if sort_by == 'completed':
            data = data.order_by('-completed', '-updated_at', '-created_at', 'priority')
        elif sort_by == 'modified_last':
            data = data.order_by('-updated_at', '-completed', '-created_at', 'priority')
        elif sort_by == 'created_last':
            data = data.order_by('-created_at', '-completed', '-updated_at', 'priority')
        elif sort_by == 'priority':
            data = data.order_by('priority', '-completed', '-updated_at', '-created_at')

    return render(request, 'index.html',{'data':data})

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
        
    project_options = ['Volvo', 'Saab', 'Mercedes', 'Audi']
    context = {
        'form': form,
        'project_options': project_options
    }
    return render(request, 'create.html', context)

def edit(request, pk):
    task=Task.objects.get(pk=pk)
    if request.POST:
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm(instance=task)

    # Retrieve the Task instance with the given pk
    task = Task.objects.get(pk=pk)
    
    if request.method == 'POST':
        # Populate the form with the POST data and the retrieved Task instance
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        # Initialize the form with the retrieved Task instance for GET requests
        form = TaskForm(instance=task)
    
    return render(request, 'edit.html', {'form': form})

def delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')


def signup(request):
    user=None
    error=None
    if request.POST:
        username = request.POST.get('username')  
        password = request.POST.get('password')
        print(username,password)
        try:
            user=User.objects.create_user(username=username,password=password)

        except Exception as e:
            error=str(e)
    return render(request,'signup.html',{'user':user,'error':error})

def login(request):
    user=None
    error=None
    if request.POST:
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('/')
        else:
            error='invalid user'
    return render(request,'login.html',{'user':user,'error':error})


def logout(request):
    authlogout(request)
    return redirect('login')