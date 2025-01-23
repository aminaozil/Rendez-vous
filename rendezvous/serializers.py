from rest_framework.serializers import ModelSerializer

from .models import RendezVous

class RendezVousSerializer(ModelSerializer):
    class Meta:
       model = RendezVous
       fields = ['pk','titre', 'date', 'heure', 'lieu', 'patient', 'medecin']