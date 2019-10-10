from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from patients.models import Patient

class TestEndpoints(APITestCase):

    def test_list_patients_is_empty(self):
        """
        Ensure we receive and empty list when there is not patients in the database.
        """
        url = reverse('patients-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list_patients_returns_patients(self):
        """
        Ensure we receive a list of patients.
        """
        patient = Patient.objects.create(
            name='mike'
        )
        patient.save()

        patient = Patient.objects.create(
            name='Arnold'
        )
        patient.save()

        url = reverse('patients-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

