from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Plant, ToDo
from .forms import PlantForm 


# Create your views here.

def plant_list_view(request):
    plant_list = Plant.objects.all()
    paginator = Paginator(plant_list, 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}  
    return render(request, 'plants/plant_list.html', context)

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

def add_plant_image_handling(request): 
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES) 
        if form.is_valid():
            new_plant = form.save()  
            # Placeholder! 
            return redirect('plant_list')  
        
def home_view(request):
    return render(request, 'plants/index.html') 

def plant_and_todo_list(request):
    return render(request, 'index.html') 

def about_view(request):
    return render(request, 'plants/about.html')