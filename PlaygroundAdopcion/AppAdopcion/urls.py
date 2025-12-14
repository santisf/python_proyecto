from django.urls import path
from AppAdopcion import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('animales/', views.cursos, name='animales_list'),
    path('animales/nuevo/', views.animal_create, name='animal_create'),
    path('adoptantes/', views.estudiantes, name='adoptantes_list'),
    path('solicitudes/', views.entregables, name='solicitudes_list'),
    path('buscar/', views.buscar, name='buscar'),
]