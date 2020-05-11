from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# pour exiger de loger avant aller au home
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Home(request):
    return render(request, 'home.html')


def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "username or password incorrect !")

        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def Register(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'bienvenue : ' + user)

                return redirect('login_view')

        context = {'form':form}
        return render(request, 'register.html', context)
