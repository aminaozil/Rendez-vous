from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Patient
from authentification.models import User

class TestPatient(APITestCase):

    url = reverse_lazy('patient-list')


    def test_list(self):
        docteur = User.objects.create(
            username = "Toulaye",
            email = "toulaye@gmail.com",
            password = "tpasser123",
        )
        patient = Patient.objects.create(id=1, nom="Diop", prenom="Coumbis", age=30, adresse="Keur massar", telephone="+22177456321",docteur_id=docteur.id)
        
        response = self.client.get(self.url)


        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': patient.pk,
                'nom': patient.nom,
                'prenom': patient.prenom,
                'age':patient.age,
                'adresse': patient.adresse, 
                'telephone': patient.telephone,
                'docteur_id': patient.docteur_id,

            }
        ]
        self.assertEqual(excepted, response.json())

        def test_create(self):
            
            self.assertFalse(Patient.objects.exists())
            response = self.client.post(self.url, data={
                "id":2, 
                "nom":"Diagnz",
                "prenom":"Ass",
                "age":30,
                "adresse":"Ngaparou",
                "telephone":"+22177456322",
                "docteur_id":"docteur.id",

            })

            self.assertEqual(response.status_code, 405)

            self.asserFalse(Patient.objects.exists())