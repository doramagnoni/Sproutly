from django.contrib import admin
from django.urls import path
from plants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plants/new', views.add_plant, name='add_plant'), 
    path('plants/todos', views.plant_and_todo_list, name='plant_and_todo_list'),
    path('plants/<int:plant_id>/edit', views.edit_plant, name='edit_plant'),
    path('plants/<int:plant_id>/delete', views.delete_plant, name='delete_plant'), 
    path('', views.home_view, name='home'),
    path('plants/', views.plant_list_view, name='plant_list'),
    path('about/', views.about_view, name='about'), 

   
]