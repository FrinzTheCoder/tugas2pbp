import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todolist.forms import NewTaskForm
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
        'list_todolist': data,
        'user': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = NewTaskForm

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Berhasil menambahkan task!')
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def update_task(request, id):
    if request.method == "POST":
        data = Task.objects.get(id=id)
        if data.is_finished == False:
            data.is_finished = True
        else:
            data.is_finished = False
        data.save()
        return redirect('todolist:show_todolist')
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    if request.method == "POST":
        data = Task.objects.get(id=id)
        data.delete()
        return redirect('todolist:show_todolist')
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)  

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

