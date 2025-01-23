from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import Patient
from rest_framework.reverse import reverse
class PatientSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="patient-details", lookup_field="pk")
    class Meta:
        model = Patient
        fields = ['url','pk','nom', 'prenom', 'age', 'adresse', 'telephone','docteur']

   


        