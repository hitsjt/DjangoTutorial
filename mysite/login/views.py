from django.shortcuts import render, redirect
from .models import User


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index')
                else:
                    message = '密码错误'
            except:
                message = '用户名不存在'
        return render(request,'login/login.html',{"message": message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect('/index/')
