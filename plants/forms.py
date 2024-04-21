from django import forms
from .models import Plant, ToDo 

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo 
        fields = ['plant', 'task_type', 'last_completed', 'due_date']
        widgets = {  
            'last_completed': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }