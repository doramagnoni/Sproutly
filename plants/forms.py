from django import forms
from .models import Plant, ToDo 

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        exclude = ['user']

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['plant', 'todo_type', 'description', 'due_date']