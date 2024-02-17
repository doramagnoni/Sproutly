from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Plant, ToDo
from .forms import PlantForm 


# Create your views here.

def plant_list(request):
    plants = Plant.objects.all()
    todos = ToDo.objects.filter(completed=False)
    return render(request, 'plants/plant_list.html', {'plants': plants, 'todos': todos})

def add_plant(request):
    if request.method == 'POST':  
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('plant_list')  
    else: 
        form = PlantForm() 
    return render(request, 'plants/add_plant.html', {'form': form})

def edit_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id) 
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)  
        form.save()  
        return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/edit_plant.html', {'form': form, 'plant': plant})

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id) 
    plant.delete()  
    return redirect('plant_list')

def confirm_delete(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/confirm_delete.html', {'plant': plant})

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES) 
        if form.is_valid():
            new_plant = form.save()  
            # Placeholder! 
            return redirect('plant_list')  
