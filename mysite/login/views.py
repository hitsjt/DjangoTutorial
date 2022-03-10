from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        login_form = UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index')
                else:
                    message = '密码错误'
            except:
                message = '用户名不存在'
        return render(request,'login/login.html',locals())
    login_form = UserForm()
    return render(request, 'login/login.html',locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect('/index/')
