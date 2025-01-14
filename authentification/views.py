from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
def logout_user(request):
    
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/info_user/")
            else:
                messages.error(request, "Email ou mot de passe incorrect")
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})


def accueil(request):
    return render(request, "index/accueil.html")

@login_required
def info_user(request):
    utilisateur = request.user
    return render(request, "authentification/info.html", {"utilisateur": utilisateur})

@login_required
def details_user(request):
    utilisateur = request.user
    return render(request, "authentification/details_user.html", {"utilisateur": utilisateur})
