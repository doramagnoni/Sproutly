from django.contrib import admin
from django.urls import path, include
from plants import views
from .views import AddPlantView, EditPlantView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Plant-related URLs
    path('plants/new', AddPlantView.as_view(), name='add_plant'),
    path('plants/todos', views.plant_and_todo_list, name='plant_and_todo_list'),
    path('todos/complete/<int:todo_id>', views.mark_todo_complete, name='mark_todo_complete'),
    path('plants/<int:pk>/edit', EditPlantView.as_view(), name='edit_plant'),
    path('plants/<int:plant_id>/delete', views.delete_plant, name='delete_plant'),
    path('plants/', views.plant_list_view, name='plant_list'),
    
    # ToDo-related URLs
    path('plants/<int:plant_id>/todos/new/', views.todo_create, name='todo_create'),  
    path('todos/<int:pk>/edit/', views.todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),

    # Home and other informational pages
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('plant-guide/', views.plant_guide, name='plant-guide'),

    # User authentication and signup
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
    path('accounts/', include('allauth.urls')),  # Allauth for extended authentication features
    path('signup/', views.signup_view, name='signup'),
]
