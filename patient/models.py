from django.db import models
from authentification.models import User

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    docteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom}"