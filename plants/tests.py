from django.test import TestCase, Client
from django.contrib.auth.models import User
from plants.models import Plant
from django.urls import reverse

class PlantModelTest(TestCase):
    """
    Test case for Plant model functionalities.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user and a plant.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        Plant.objects.create(
            name="Golden Pothos",
            species="Epipremnum aureum",
            watering_interval=7,
            fertilization_interval=30,
            user=self.user
        )

    def test_creating_a_plant(self):
        """
        Test the creation and retrieval of a Plant object.
        """
        plant = Plant.objects.get(name="Golden Pothos")
        self.assertEqual(plant.species, "Epipremnum aureum")
        self.assertEqual(plant.watering_interval, 7)

class SignupTestCase(TestCase):
    """
    Test case for user signup functionality.
    """

    def test_successful_signup(self):
        """
        Test the signup process with valid data.
        """
        client = Client()
        response = client.post(reverse('signup'), data={
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_unsuccessful_signup(self):
        """
        Test the signup process with invalid data.
        """
        client = Client()
        response = client.post(reverse('signup'), data={
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'testpassword123',
            'password2': 'mismatchpassword'
        })
        self.assertEqual(response.status_code, 200)  # Check for validation errors
        self.assertFalse(User.objects.filter(username='testuser').exists())
