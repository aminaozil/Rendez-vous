from rest_framework import serializers

from .models import RendezVous

class RendezVousSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="details-rendezvous", lookup_field="pk")
    class Meta:
       model = RendezVous
       fields = ['pk','titre', 'date', 'heure', 'lieu', 'patient', 'medecin']