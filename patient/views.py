from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .form import PatientForm
from django.core.paginator import Paginator
from .models import Patient

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .serializers import PatientSerializer

class PatientViewset(ReadOnlyModelViewSet):
    serializer_class = PatientSerializer


    def get_queryset(self):
        queryset = Patient.objects.all()
        


        
        docteur_id = self.request.GET.get('docteur_id')
        if docteur_id is not None:
            queryset = queryset.filter(docteur_id=docteur_id)


        return queryset



@login_required(login_url="login")
def list_patient(request):
    utilisateur = request.user
   
    patient_user = Patient.objects.filter(docteur=utilisateur)
    nbr_patient = Patient.objects.filter(docteur=utilisateur).count()

    paginator = Paginator(patient_user, 4)
    page_number = request.GET.get('page')
    patientuser  = paginator.get_page(page_number)

    if request.user.is_superuser:
        patientus = Patient.objects.all()
        paginator = Paginator(patientus, 4)
        page_number = request.GET.get('page')
        patientuser  = paginator.get_page(page_number)
    

    if request.method == "GET":
        name = request.GET.get("recherche")
        if name is not None:
            patientuser = Patient.objects.filter(docteur=utilisateur).filter(prenom__icontains=name)

    

    return render(request, "patient/list_patient.html",{'patient_user':patient_user,"patientuser":patientuser, "utilisateur":utilisateur, "nbr_patient":nbr_patient})
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
@permission_required("patient.change_patient" , raise_exception=True)
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
