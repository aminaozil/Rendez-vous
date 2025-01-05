from django.shortcuts import render, redirect
from .models import Docteur

def add_docteur(request):
    if request.method == "POST":
        photo = request.FILES['photo']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']
        email = request.POST['email']
        password = request.POST['password']
        specialite = request.POST['specialite']
        docteur = Docteur.objects.create(
            photo=photo,
            nom=nom,
            prenom=prenom,
            adresse=adresse,
            telephone=telephone,
            email=email,
            password=password,
            specialite=specialite,
        )
        docteur.save()
        return redirect("/test/")

    return render(request, "docteur/add_docteur.html")
def details_docteur(request):
    return render(request, "docteur/details_docteur.html")