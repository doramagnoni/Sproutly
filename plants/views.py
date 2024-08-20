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

# View for listing plants with pagination
def plant_list_view(request):
    # Filter plants to include only those created by the logged-in user
    plant_list = Plant.objects.filter(user=request.user)
    
    # Set up pagination: 25 plants per page
    paginator = Paginator(plant_list, 25)
    page_number = request.GET.get('page', 1)  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the plants for the current page
    
    # Context to pass to the template
    context = {'page_obj': page_obj}
    return render(request, 'plants/plant_list.html', context)

@login_required
def delete_plant(request, plant_id):
    # Retrieve the plant object or return 404 if not found
    plant = get_object_or_404(Plant, pk=plant_id, user=request.user)
    
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    
    # Render the plant deletion confirmation page
    return render(request, 'plants/plant_confirm_delete.html', {'plant': plant})

@login_required
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user  # Associate the plant with the current user
            plant.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    
    # Render the plant creation form
    return render(request, 'plants/plant_form.html', {'form': form})

def home_view(request):
    # Render the home page
    return render(request, 'plants/index.html')

@login_required
def plant_and_todo_list(request):
    # Filter plants to include only those created by the logged-in user
    plants = Plant.objects.filter(user=request.user)
    
    if not plants.exists():
        context = {'has_plants': False}
    else:
        # Retrieve todos associated with the user's plants
        todos = ToDo.objects.filter(plant__in=plants)
        context = {
            'has_plants': True,
            'plant_todos': [
                {'plant': plant, 'todos': todos.filter(plant=plant)}
                for plant in plants
            ]
        }
    
    # Render the template with the plant and todo list
    return render(request, 'plants/todo_template.html', context)

@login_required
def mark_todo_complete(request, todo_id):
    if request.method == "POST":
        # Retrieve the to-do item or return 404 if not found
        todo = get_object_or_404(ToDo, pk=todo_id)
        if todo.plant.user == request.user:  # Ensure the to-do item belongs to the current user
            todo.completed = not todo.completed
            todo.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Not authorized'}, status=403)
    else:
        return redirect('plant_and_todo_list')

@login_required
def todo_create(request, plant_id):
    # Retrieve the plant object or return 404 if not found
    plant = get_object_or_404(Plant, pk=plant_id, user=request.user)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.plant = plant  # Associate the ToDo with the plant
            todo.save()
            return redirect('plant_and_todo_list')
    else:
        form = ToDoForm()
    
    # Render the to-do creation form
    return render(request, 'plants/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    # Retrieve the to-do item or return 404 if not found
    todo = get_object_or_404(ToDo, pk=pk)
    
    if todo.plant.user != request.user:  # Ensure the to-do item belongs to the current user
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('plant_and_todo_list')
    else:
        form = ToDoForm(instance=todo)
    
    # Render the to-do update form
    return render(request, 'plants/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    # Retrieve the to-do item or return 404 if not found
    todo = get_object_or_404(ToDo, pk=pk)
    
    if todo.plant.user != request.user:  # Ensure the to-do item belongs to the current user
        return redirect('access_denied')
    
    if request.method == 'POST':
        todo.delete()
        return redirect('plant_and_todo_list')
    
    # Render the to-do deletion confirmation page
    return render(request, 'plants/todo_confirm_delete.html', {'todo': todo})

def about_view(request):
    # Render the about page
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
    
    # Render the user registration form
    return render(request, 'registration/signup.html', {'form': form})

def plant_guide(request):
    # Render the plant guide page
    return render(request, 'plants/plant-guide.html')

class AddPlantView(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html'
    success_url = reverse_lazy('plant_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associate the plant with the current user
        return super().form_valid(form)

class EditPlantView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'plants/plant_form.html'
    success_url = reverse_lazy('plant_list')

    def get_queryset(self):
        # Allow users to edit only their own plants
        return Plant.objects.filter(user=self.request.user)
