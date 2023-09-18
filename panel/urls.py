from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('dashboard', views.dashboard, name="Admin Dashboard"),

    path('view_client', views.view_client, name="view_client"),
    path('add_client', views.add_client, name="add_client"),
    path('delete_client', views.delete_client, name="delete_client"),
    path('edit_client', views.edit_client, name="edit_client"),

    path('add_trainer', views.add_trainer, name="add_trainer"),
    path('trainers', views.trainers, name="trainers"),
    path('delete_trainer', views.delete_trainer, name="delete_trainer"),
    path('edit_trainer', views.edit_trainer, name="edit_trainer"),

    path('trainers_requests', views.trainers_requests, name="trainers_requests"),

    path('add_programcategory', views.add_programcategory, name="add_programcategory"),
    path('delete_category', views.delete_category, name="delete_category"),
    path('edit_category', views.edit_category, name="edit_category"),

    path('add_training_program', views.add_training_program, name="add_training_program"),
    path('training_programs', views.training_programs, name="training_programs"),
    path('delete_program', views.delete_program, name="delete_program"),
    path('edit_program', views.edit_program, name="edit_program"),
    
]