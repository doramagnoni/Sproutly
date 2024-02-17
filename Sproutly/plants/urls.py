from django.contrib import admin
from django.urls import path
from plants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plant_list, name='plant_list'),
    path('plants/new', views.add_plant, name='add_plant'), 
    path('plants/<int:plant_id>/edit', views.edit_plant, name='edit_plant'),
    path('plants/<int:plant_id>/delete', views.delete_plant, name='delete_plant'), 
    
]