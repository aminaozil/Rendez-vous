from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import User


class TestUser(APITestCase):

    url = reverse_lazy('user-list')

    def test_list(self):
        user = User.objects.create(last_name="Passer2", first_name="Ndiaye",email="passer@gmail.com")

        response = self.client.get(self.url)


        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                
                
                'last_name': user.last_name,
                'first_name':user.first_name,
                'email': user.email,
                

            }
        ]
        self.assertEqual(excepted, response.json())

    

