from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    species = models.CharField(max_length=100)
    description = models.TextField(default="No description provided")
    watering_interval = models.IntegerField(help_text="Days between watering")
    light_requirements = models.CharField(max_length=100, default="Unknown Light Requirements")
    last_watered = models.DateField(auto_now_add=True) 
    fertilization_interval = models.IntegerField(help_text="Days between fertilization")
    last_fertilized = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='plant_images', default='plant_images/default_plant.jpg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    
    def __str__(self):
      return self.name 


class ToDo(models.Model):
    TODO_TYPE_CHOICES = [
        ('watering', 'Watering'),
        ('fertilization', 'Fertilization'),
    ]

    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='todos')
    todo_type = models.CharField(max_length=20, choices=TODO_TYPE_CHOICES, default='watering') 
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.todo_type.capitalize()} for {self.plant.name} on {self.due_date}"