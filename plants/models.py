from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Plant(models.Model):
    # The name of the plant
    name = models.CharField(max_length=100, null=False, blank=False)
    
    # The species of the plant
    species = models.CharField(max_length=100)
    
    # A description of the plant
    description = models.TextField(default="No description provided")
    
    # Interval in days between each watering
    watering_interval = models.IntegerField(help_text="Days between watering")
    
    # Light requirements of the plant
    light_requirements = models.CharField(max_length=100, default="Unknown Light Requirements")
    
    # Date when the plant was last watered
    last_watered = models.DateField(auto_now_add=True)
    
    # Interval in days between each fertilization
    fertilization_interval = models.IntegerField(help_text="Days between fertilization")
    
    # Date when the plant was last fertilized
    last_fertilized = models.DateField(auto_now_add=True)
    
    # Image of the plant
    image = models.ImageField(upload_to='plant_images', default='plant_images/default_plant.jpg')
    
    # User associated with the plant
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

class ToDo(models.Model):
    # Choices for the type of to-do item
    TODO_TYPE_CHOICES = [
        ('watering', 'Watering'),
        ('fertilization', 'Fertilization'),
    ]
    
    # The plant associated with the to-do item
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='todos')
    
    # The type of to-do item
    todo_type = models.CharField(max_length=20, choices=TODO_TYPE_CHOICES, default='watering')
    
    # Description of the to-do item
    description = models.TextField(blank=True)
    
    # Due date for the to-do item
    due_date = models.DateField()
    
    # Status indicating if the to-do item is completed
    completed = models.BooleanField(default=False)
    
    # Timestamp when the to-do item was created
    created_at = models.DateTimeField(default=timezone.now)
    
    # Timestamp when the to-do item was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.todo_type.capitalize()} for {self.plant.name} on {self.due_date}"
