from django.shortcuts import get_object_or_404, render, redirect
from authentification.models import User
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from .models import RendezVous
from .forms import RendezVousForm


@login_required
def add_rv(request):
    form = RendezVousForm()
    if request.method == "POST":
        form = RendezVousForm(request.POST)
        medecin = request.user
        titre = request.POST['titre']
        patient = Patient.objects.get(pk=request.POST['patient'])
        date  = request.POST['date']
        heure = request.POST['heure']
        lieu = request.POST['lieu']
        rendez_vous = RendezVous.objects.create(
            medecin = medecin,
            titre = titre,
            patient = patient,
            date = date,
            heure = heure,
            lieu = lieu,

        )
        # re = RendezVous.objects.filter(request.POST["date"]).exists(True)
        # if re:
        #     rendez_vous.save()
            
        # else:
        #     mes = "date existe déja"
            
        rendez_vous.save()
        return redirect("/list_rendezvous/")
   
        
    return render(request, "rendez/add_rendez.html", {"form": form}) 
@login_required
def list_rv(request):
    utilisateur = request.user
    rendez_user = RendezVous.objects.filter(medecin=utilisateur)
    nbr_rendez = RendezVous.objects.filter(medecin=utilisateur).count()



    return render(request, "rendez/list_rv.html", {"rendez_user":rendez_user, "utilisateur":utilisateur, "nbr_rendez":nbr_rendez})

def details_rendez(request, id):
    rendez = get_object_or_404(RendezVous, id=id) 
    return render(request, "rendez/details_rendez.html", {"rendez":rendez}) 