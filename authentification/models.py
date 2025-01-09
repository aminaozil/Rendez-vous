from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    adresse = models.CharField(max_length=255, null=True, verbose_name="adresse")
    telephone = models.CharField(max_length=255, verbose_name="telephone")
    specialite = models.CharField(max_length=255, verbose_name="specialite")
    photo_profil = models.ImageField(verbose_name='Photo profile', null=True)