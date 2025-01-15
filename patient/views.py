from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import admin
from .form import PatientForm
from .models import Patient
from authentification.models import User


@login_required(login_url="login")
def list_patient(request):
    utilisateur = request.user
   
    patient_user = Patient.objects.filter(docteur=utilisateur)

    if request.method == "GET":
        name = request.GET.get("recherche")
        if name is not None:
            patient_user = Patient.objects.filter(docteur=utilisateur).filter(prenom__icontains=name)

    

    return render(request, "patient/list_patient.html",{'patient_user':patient_user, "utilisateur":utilisateur})
@login_required
@permission_required("patient.add_patient" , raise_exception=True)
def add_patient(request):
    forms = PatientForm(request.POST)
    if request.method == "POST":
        docteur = request.user
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        age = request.POST['age']
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']

        patients = Patient.objects.create(
            docteur = docteur,
            nom = nom,
            prenom = prenom,
            age = age,
            adresse = adresse,
            telephone = telephone,

        )
        patients.save()
        return redirect("/list_patient/")
    
    forms = PatientForm()

    return render(request, "patient/add_patient.html", {"forms": forms})
@login_required
def edit_patient(request, id):
    patient_edit = Patient.objects.get(id=id)
    forms = PatientForm(request.POST or None, instance=patient_edit)
    if forms.is_valid():
        forms.save()
        return redirect("/list_patient/")
    
    

    return render(request, "patient/edit_patient.html", {"forms":forms})
@login_required
def details_patient(request,id): 
    patient = get_object_or_404(Patient, id=id)
    return render(request, "patient/details.html",{"patient": patient})
