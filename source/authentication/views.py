from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication.forms import LoginForm, SignUpForm


# Create your views here.
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie...')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home')
            else:
                messages.success(request, 'Erreur d\'authentification! Réessayer...')
    return render(request, 'authentication/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'authentication/register.html', {'form': form})

