from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserLogInForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout


def LoginView(request):
    '''
    Обработчик авторизации пользователя.
    '''
    if request.method == 'POST':
        user_form = UserLogInForm(request.POST)
        if user_form.is_valid():
            form_data = user_form.cleaned_data
            user = authenticate(request, username=form_data['username'], password=form_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('user_profile:profile'))
                else:
                    return HttpResponse('Disabled account!')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLogInForm()
    
    return render(request, 'user_auth/login.html', {'form': form})


def RegisterView(request):
    '''
    Обработчик регистрации пользователя.
    '''
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return HttpResponseRedirect(reverse('user_profile:profile'))
    else:
        user_form = UserRegisterForm
    context = {'form': user_form}
    return render(request, 'user_auth/signup.html', context)    


def UserLogOutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_auth:login'))