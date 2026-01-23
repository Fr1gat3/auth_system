from django.shortcuts import render

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'form': UserRegistrationForm()}
    return render(request, 'users/register.html', context)
