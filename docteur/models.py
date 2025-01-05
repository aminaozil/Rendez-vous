from django.db import models

class Docteur(models.Model):
    photo = models.ImageField(upload_to='images/')
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom}"
    