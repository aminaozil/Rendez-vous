from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Patient

class TestPatient(APITestCase):

    url = reverse_lazy('patient_list')


    def test_list(self):
        patient = Patient.objects.create()

        response = self.client.get(self.url)


        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': patient.pk,
                'prenom': patient.prenom,
                'nom': patient.nom,
                'age':patient.age,
                'adresse': patient.adresse, 
                'telephone': patient.telephone,

            }
        ]
        self.assertEqual(excepted, response.json())