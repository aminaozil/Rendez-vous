from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    adresse = models.CharField(max_length=250, null=True, verbose_name="adresse")
    telephone = models.CharField(max_length=250, verbose_name="telephone")
    specialite = models.CharField(max_length=250, verbose_name="specialite")
    photo_profil = models.ImageField(verbose_name='Photo profile', null=True)
    email = models.EmailField(unique=True, max_length=250)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
#verifie si le password n'est pas hassher de le faire
    def save(self, *args, **kwargs):
   
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
        
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"