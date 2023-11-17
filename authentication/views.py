from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render

from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'You are logged'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

def logout_def(request):
    logout(request)
    message = 'User disconnected'
    form = forms.LoginForm()  # Create a new instance of the login form
    return render(request, 'authentication/login.html', {'message': message, 'form': form})