from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ChargingStation

class ChargingStationTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a charging station
        self.charging_station = ChargingStation.objects.create(
            name='Test Charging Station',
            address='Test Address',
            owner=self.user,
        )

    def test_charging_station_creation(self):
        # Verify that the charging station is created successfully
        self.assertEqual(self.charging_station.name, 'Test Charging Station')
        self.assertEqual(self.charging_station.address, 'Test Address')
        self.assertEqual(self.charging_station.owner, self.user)

    def test_authentication_required(self):
        # Verify that authentication is required to access the charging station creation page
        response = self.client.get(reverse('create_charging_station'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/create_charging_station/')

    def test_create_charging_station(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Submit a POST request to create a new charging station
        response = self.client.post(reverse('create_charging_station'), {
            'name': 'New Charging Station',
            'address': 'New Address',
        })

        # Verify that the charging station is created and the user is redirected
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ChargingStation.objects.filter(name='New Charging Station').exists(), True)

    def test_nearby_charging_stations(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Access the nearby charging stations page
        response = self.client.get(reverse('nearby_charging_stations'))

        # Verify that the response is successful
        self.assertEqual(response.status_code, 200)

        # Verify that the charging station is listed
        self.assertContains(response, 'Test Charging Station')
