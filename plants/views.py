from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Plant, ToDo
from .forms import PlantForm, ToDoForm
from django.views.generic import CreateView, UpdateView  

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

    context = {
        'plant_todos': []
    }

    for plant in plants:
        plant_data = {
            'plant': plant,
            'todos': todos.filter(plant=plant)
        }
        context['plant_todos'].append(plant_data)

    return render(request, 'plants/todo_template.html', context)

def mark_todo_complete(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(ToDo, pk=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({'success': True})
    else:
        return redirect('plant_and_todo_list')

@login_required
def todo_create(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.plant = plant  # Link the ToDo to this specific plant
            todo.save()
            return redirect('plant_and_todo_list')
    else:
        form = ToDoForm()
    return render(request, 'plants/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('plant_and_todo_list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'plants/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('plant_and_todo_list')
    return render(request, 'plants/todo_confirm_delete.html', {'todo': todo})

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
