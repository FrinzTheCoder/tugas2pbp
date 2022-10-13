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
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    form = NewTaskForm
    context = {
        'user': request.user.username,
        'last_login': request.COOKIES['last_login'],
        'form':form
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
@csrf_exempt
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

def get_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("description")
        user = request.user

        new_task = Task(title=title, description=desc, user=user)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# def delete_ajax(request):
#     if request.method == "POST":
#         id = request.POST.get("id")
#         print(id)
#         data = Task.objects.get(id=id)
#         data.delete()
#         return HttpResponse(b"DELETED", status=204)
