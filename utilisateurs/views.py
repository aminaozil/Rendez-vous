from django.shortcuts import render

def test(request):
    return render(request, "rendez/test.html")

def login_view(request):
    return render(request, "utilisateurs/login.html")

def register_view(request):
    return render(request, "utilisateurs/register.html")
def dashboard(request):
    return render(request, "partials/dashboard.html")