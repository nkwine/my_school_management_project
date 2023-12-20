from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django  .contrib import  messages


# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None and user.type =='teacher':
            login(request, user)
            return redirect('teacher')
        elif user is not None and user.type =='dos':
            login(request, user)
            return redirect('dos')
        elif user is not None and user.type =='secretary':
            login(request, user)
            return redirect('secretary')
        elif user is not None and user.type =='bursar':
            login(request, user)
            return redirect('bursar')
        elif user is not None and user.type =='head':
            login(request, user)
            return redirect('head')
        elif user is not None and user.type =='student':
            login(request, user)
            return redirect('student')
        elif user is not None and user.is_superuser:
            login(request,user)
            return redirect('admini/home')
    return render(request,'login.html',{})
