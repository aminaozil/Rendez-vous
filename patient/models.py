from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)