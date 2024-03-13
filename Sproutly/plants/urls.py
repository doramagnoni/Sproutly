from django.contrib import admin
from django.urls import path, include
from plants import views
from .views import AddPlantView
from .views import AddPlantView, EditPlantView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plants/new', AddPlantView.as_view(), name='add_plant'),
    path('plants/todos', views.plant_and_todo_list, name='plant_and_todo_list'),
    path('todos/complete/<int:todo_id>', views.mark_todo_complete, name='mark_todo_complete'),
    path('plants/<int:pk>/edit', EditPlantView.as_view(), name='edit_plant'), 
    path('plants/<int:plant_id>/delete', views.delete_plant, name='delete_plant'), 
    path('', views.home_view, name='home'),
    path('plants/', views.plant_list_view, name='plant_list'),
    path('about/', views.about_view, name='about'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('plant-guide/', views.plant_guide, name='plant-guide')

]