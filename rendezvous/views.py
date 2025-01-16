from django.shortcuts import get_object_or_404, render, redirect
from authentification.models import User
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from .models import RendezVous
from django.http import HttpResponse
from django.utils import timezone


@login_required
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
            return HttpResponse("Il y a déjà un rendez-vous pour ce médecin à cette heure.", status=400)
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
            return redirect("rendezvous/list_rendezvous") 
    else:
        # Formulaire de création
        medecins = User.objects.all()
        patients = Patient.objects.all()
        return render(request, 'rendez/add_rendez.html', {'medecins': medecins, 'patients':patients}) 
   
        
@login_required
def list_rv(request):
    utilisateur = request.user
    rendez_user = RendezVous.objects.filter(medecin=utilisateur)
    nbr_rendez = RendezVous.objects.filter(medecin=utilisateur).count()



    return render(request, "rendez/list_rv.html", {"rendez_user":rendez_user, "utilisateur":utilisateur, "nbr_rendez":nbr_rendez})

def details_rendez(request, id):
    rendez = get_object_or_404(RendezVous, id=id) 
    return render(request, "rendez/details_rendez.html", {"rendez":rendez}) 