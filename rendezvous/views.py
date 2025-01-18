from django.shortcuts import get_object_or_404, render, redirect
from authentification.models import User
from django.contrib.auth.decorators import login_required, permission_required
from patient.models import Patient
from .models import RendezVous
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator


@login_required
@permission_required("rendezvous.add_rendezvous" , raise_exception=True)
def add_rv(request):
    if request.method == "POST":
        medecin_id = request.POST.get('medecin_id')
        patient_id = request.POST.get('patient_id')
        titre = request.POST.get('titre')  
        date = request.POST.get('date')  
        heure = request.POST.get('heure')
        lieu = request.POST.get('lieu')

        # Convertir la chaîne de date/heure en un objet datetime
        try:
            date = timezone.datetime.strptime(date, '%Y-%m-%d')
            heure = timezone.datetime.strptime(heure, '%H:%M')

        except ValueError:
            return HttpResponse("Le format choisi est invalide.", status=400)

        # Vérifier si un rendez-vous existe déjà pour ce médecin à cette date
        existe_rdv = RendezVous.objects.filter(medecin_id=medecin_id, date=date, heure=heure).exists()

        if existe_rdv:
            return HttpResponse("ce medecin a déjà un rendez-vous à cette heure.", status=400)
        else:
            # Créer un nouveau rendez-vous
            medecin = User.objects.get(id=medecin_id)
            patient = Patient.objects.get(id=patient_id)
            RendezVous.objects.create(
                medecin=medecin,
                patient=patient,
                titre=titre,
                date=date,
                heure=heure,
                lieu=lieu,
                
            )
            return redirect("list_rendezvous") 
    else:
        # Formulaire de création
        medecins = User.objects.all()
        patients = Patient.objects.all()
        return render(request, 'rendez/add_rendez.html', {'medecins': medecins, 'patients':patients}) 
   

@login_required
@permission_required("rendezvous.edit_rendezvous" , raise_exception=True)
def edit_rv(request, id):
    rendez = get_object_or_404(RendezVous, id=id)
    if request.method == "POST":
        medecin_id = request.POST.get('medecin_id')
        patient_id = request.POST.get('patient_id')
        titre = request.POST.get('titre')  
        date = request.POST.get('date')  
        heure = request.POST.get('heure')
        lieu = request.POST.get('lieu')

        # Convertir la chaîne de date/heure en un objet datetime
        try:
            date = timezone.datetime.strptime(date, '%Y-%m-%d')
            heure = timezone.datetime.strptime(heure, '%H:%M')

        except ValueError:
            return HttpResponse("Le format choisi est invalide.", status=400)

        # Vérifier si un rendez-vous existe déjà pour ce médecin à cette date
        
            # Créer un nouveau rendez-vous
        medecin = User.objects.get(id=medecin_id)
        patient = Patient.objects.get(id=patient_id)

        modif = RendezVous.objects.filter(pk=rendez.id)
        modif.update(
            medecin=medecin,
            patient=patient,
            titre=titre,
            date=date,
            heure=heure,
            lieu=lieu
                
            )
        return redirect("list_rendezvous") 
    else:
        # Formulaire de création
        medecins = User.objects.all()
        patients = Patient.objects.all()

    return render(request, "rendez/edit_rendez.html", {"rendez":rendez, "medecins":medecins, "patients":patients})       

@login_required
def list_rv(request):
    utilisateur = request.user
    rendez_user = RendezVous.objects.filter(medecin=utilisateur)
    nbr_rendez = RendezVous.objects.filter(medecin=utilisateur).count()

    paginator = Paginator(rendez_user, 4)
    page_number = request.GET.get('page')
    rendez_user  = paginator.get_page(page_number)
    if request.user.is_superuser:
        rendez_user= RendezVous.objects.all()
        paginator = Paginator(rendez_user, 4)
        page_number = request.GET.get('page')
        rendez_user  = paginator.get_page(page_number)
    

    return render(request, "rendez/list_rv.html", {"rendez_user":rendez_user, "utilisateur":utilisateur, "nbr_rendez":nbr_rendez})

def details_rendez(request, id):
    rendez = get_object_or_404(RendezVous, id=id) 
    return render(request, "rendez/details_rendez.html", {"rendez":rendez}) 