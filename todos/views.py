from django.shortcuts import render,redirect
from . models import Todo
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    todos=Todo.objects.all().filter(created_by=request.user)
    return render(request,'todos/home.html',{'todos':todos})
def todo(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        todo=Todo.objects.create(title=title,content=content,created_by=request.user)
        todo.save()
        return redirect('/')
def content(request,Todo_id):
    todo=Todo.objects.get(pk=Todo_id)
    return render(request,'todos/content.html',{'todo':todo})

def delete(request,Todo_id):
    todo=Todo.objects.get(pk=Todo_id)
    todo.delete()
    return redirect('/')

def edit(request,Todo_id):
    todo=Todo.objects.get(pk=Todo_id)
    return render(request,'todos/edit.html',{'todo':todo})

def update(request,Todo_id):
    todo=Todo.objects.get(id=Todo_id)
    if request.method=='POST':
     todo.title=request.POST['title']
     todo.content=request.POST['content']
     todo.save()
     return redirect('/')
    return render(request,'todos/home.html')
def finish(request,Todo_id):
    todo=Todo.objects.get(id=Todo_id)
    todo.status=True
    todo.save()
    return redirect('/')
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken, use another username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already used . please use another email')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info("The two password are not a match please reenter the password")
            return redirect('register')
    return render(request,'todos/register.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'todos/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')



# Create your views here.
