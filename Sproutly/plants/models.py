from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(default="No description provided")
    watering_interval = models.IntegerField(help_text="Days between watering")
    light_requirements = models.CharField(max_length=100, default="Unknown Light Requirements")
    last_watered = models.DateField(auto_now_add=True) 
    fertilization_interval = models.IntegerField(help_text="Days between fertilization")
    last_fertilized = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='plant_images', default='plant_images/default_plant.jpg')


class ToDo(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20, choices=[('WATER', 'Water'), ('FERTILIZE', 'Fertilize')])
    due_date = models.DateField()
    completed = models.BooleanField(default=False)