from django.shortcuts import render, redirect, get_object_or_404

import docteur
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

def edit_docteur(request, id):
    docteur = get_object_or_404(Docteur, id=id)
    try:

        if request.method == "POST":
            photo = request.FILES['photo']
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            adresse = request.POST['adresse']
            telephone = request.POST['telephone']
            email = request.POST['email']
            password = request.POST['password']
            specialite = request.POST['specialite']
            update_docteur = Docteur.objects.filter(pk=docteur.id)
            update_docteur.update(
                photo=photo,
                nom=nom,
                prenom=prenom,
                adresse=adresse,
                telephone=telephone,
                email=email,
                password=password,
                specialite=specialite,

            )
            
            
            return redirect("/test/")
    except Exception:
        print("pas de changement")

    return render(request, "docteur/edit_docteur.html", {"docteur":docteur})


def details_docteur(request, id):
    docteurs = Docteur.objects.get(id=id)


    return render(request, "docteur/details_docteur.html", {"docteurs": docteurs})

def delete_docteur(request, id):
    docteur = get_object_or_404(Docteur, id=id)
    if request.method == "POST":
        docteur_delete = Docteur.objects.filter(pk=docteur.id)
        docteur_delete.update(
            archive=True
        )
    return redirect("/list/")

def list_docteur(request):
    docteurs = Docteur.objects.filter(archive=False)
    return render(request, "docteur/list_docteur.html",{"docteurs": docteurs})

def info_docteur(request):
    use = request.user
    docteurs = Docteur.objects.filter(archive=False)

    return render(request, "docteur/info.html", {"docteurs": docteurs, "user":use})