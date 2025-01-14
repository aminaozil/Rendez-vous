from django.db import models
from authentification.models import User
from patient.models import Patient


class RendezVous(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=255)
    medecin = models.ForeignKey(User,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.titre}"