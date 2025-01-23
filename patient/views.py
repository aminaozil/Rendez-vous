from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .form import PatientForm
from django.core.paginator import Paginator
from .models import Patient

from rest_framework import generics
from .serializers import PatientSerializer
from api.mixins import StaffPermissionsMixin

class PatientListApiView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    

    def get_queryset(self):
        queryset = Patient.objects.filter(docteur=self.request.user.id)
        if self.request.user.is_staff:
            queryset = Patient.objects.all()
        return queryset


class PatientRetrieveApiView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pk'

class PatientUpdateApiView(StaffPermissionsMixin,
                           generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        nom = serializer.validated_data.get("nom")
        prenom = serializer.validated_data.get("prenom")
        age = serializer.validated_data.get("age")
        adresse = serializer.validated_data.get("adresse")
        telephone = serializer.validated_data.get("telephone")
        docteur_id = serializer.validated_data.get("docteur_id")

        serializer.save()


class PatientDeleteApiView(StaffPermissionsMixin,
                           generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pk'


class PatientCreateApiView(StaffPermissionsMixin,
                           generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        nom = serializer.validated_data.get("nom")
        prenom = serializer.validated_data.get("prenom")
        age = serializer.validated_data.get("age")
        adresse = serializer.validated_data.get("adresse")
        telephone = serializer.validated_data.get("telephone")
        docteur_id = serializer.validated_data.get("docteur_id")

        return serializer.save()




        



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
