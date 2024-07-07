from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'Register/index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'Register/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('user')
            elif user is not None and user.is_trainer:
                login(request, user)
                return redirect('trainer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'Register/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'Register/admin.html')


def user(request):
    return render(request,'Register/user.html')


def trainer(request):
    return render(request,'Register/trainer.html')


def logout_view(request):
    logout(request)
    return redirect('index')