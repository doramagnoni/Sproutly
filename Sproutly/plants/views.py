from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Plant, ToDo
from .forms import PlantForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

def plant_list_view(request):
    plant_list = Plant.objects.all()
    paginator = Paginator(plant_list, 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}  
    return render(request, 'plants/plant_list.html', context)


def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id) 
    plant.delete()  
    return redirect('plant_list')


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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def plant_guide(request):
    return render(request, 'plants/plant-guide.html')

class AddPlantView(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html' 
    success_url = reverse_lazy('plant_list') 

class EditPlantView(UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html' 
    success_url = reverse_lazy('plant_list') 