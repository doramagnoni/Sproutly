from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Plant, ToDo
from .forms import PlantForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse

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
    if plant.user != request.user:  
        return redirect('access_denied')  
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

@login_required
def plant_and_todo_list(request):
    plants = Plant.objects.filter(user_id=request.user.id)
    todos = ToDo.objects.filter(plant__in=plants)

    print("All todos:", todos)  # Add this line

    context = {
        'plant_todos': []
    }

    for plant in plants:
        plant_data = {
            'plant': plant,
            'todos': todos.filter(plant=plant)
        }
        context['plant_todos'].append(plant_data)

        print(f"Todos for plant {plant}:")  
        for todo in plant_data['todos']: 
            print(f"  - Task: {todo.task_type}, Completed: {todo.completed}")  

    return render(request, 'plants/todo_template.html', context)

def mark_todo_complete(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(ToDo, pk=todo_id) 
        todo.completed = not todo.completed

        if todo.completed: 
            if todo.task_type == 'WATER':
                todo.task_type = 'WATERED' 
            elif todo.task_type == 'FERTILIZE':
                todo.task_type = 'FERTILIZED'

        todo.save()
        return JsonResponse({'success': True}) 
    else:
        return redirect('plant_and_todo_list')

def about_view(request):
    return render(request, 'plants/about.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def plant_guide(request):
    return render(request, 'plants/plant-guide.html')

class AddPlantView(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html' 
    success_url = reverse_lazy('plant_list') 

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class EditPlantView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html' 
    success_url = reverse_lazy('plant_list') 

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user) 