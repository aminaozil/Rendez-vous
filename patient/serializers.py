from rest_framework.serializers import ModelSerializer


from .models import Patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['nom', 'prenom', 'age', 'adresse', 'telephone','docteur']

        