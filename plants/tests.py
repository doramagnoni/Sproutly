from django.test import TestCase
from django.contrib.auth.models import User
from plants.models import Plant
from django.shortcuts import reverse
from django.test import Client  

class PlantModelTest(TestCase):

    def setUp(self):  
        user = User.objects.create_user(username='testuser', password='testpassword')
        user.save() 
        Plant.objects.create(
            name="Golden Pothos", 
            species="Epipremnum aureum", 
            watering_interval=7, 
            fertilization_interval=30, 
            user=user)  

    def test_creating_a_plant(self):
        plant = Plant.objects.get(name="Golden Pothos")
        self.assertEqual(plant.species, "Epipremnum aureum")
        self.assertEqual(plant.watering_interval, 7)

class SignupTestCase(TestCase):

    def test_successful_signup(self):
        client = Client()  
        response = client.post(reverse('signup'), data={
            'username': 'testuser', 
            'email': 'test@test.com', 
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(User.objects.filter(username='testuser').exists())
