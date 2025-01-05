from django.contrib import messages
from django.shortcuts import redirect, render


def test(request):
    return render(request, "rendez/test.html")

def accueil(request):
    return render(request, "utilisateurs/acceuil.html")


def register_view(request):
    return render(request, "utilisateurs/register.html")
def dashboard(request):
    return render(request, "partials/dashboard.html")

def login_view(request):
    if request.method == "POST":
        
        email = request.POST['email']
        password = request.POST['password']
        
        if email == "anta@gmail.com" and password == "yum12345":
            
            return redirect("/utilisateur/test/")
        else: 
            messages.error(request, "Email ou mot de passe incorrect.")
    return render(request, "utilisateurs/login.html")