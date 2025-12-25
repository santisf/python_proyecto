"""from django.urls import path
from core import views_clases
from .views_clases import AdoptanteCreateView, AdoptanteDetailView, AdoptanteListView, BuscarAnimalView

urlpatterns = [
    path("tienda/", views_clases.TiendaView.as_view(), name="tienda"),
    path('', views_clases.InicioView.as_view(), name='inicio'),
    path('animales/', views_clases.AnimalListView.as_view(), name='animales_list'),
    path("animales/nuevo/", views_clases.AnimalCreateView.as_view(), name="animal_create"),
    path("adoptantes/nuevo/", views_clases.AdoptanteCreateView.as_view(), name="adoptante_create"),
    path("solicitudes/nuevo/", views_clases.SolicitudCreateView.as_view(), name="solicitud_create"),
    path('adoptantes/', views_clases.AdoptanteListView.as_view(), name='adoptantes_list'),
    path('solicitudes/', views_clases.SolicitudListView.as_view(), name='solicitudes_list'),
    path("buscar/", BuscarAnimalView.as_view(), name="buscar"),

    path('adoptantes/', AdoptanteListView.as_view(), name='adoptantes_list'), 
    path('adoptantes/<int:pk>/', AdoptanteDetailView.as_view(), name='adoptante_detail'), 
    

    path("animales/<int:pk>/", views_clases.AnimalDetailView.as_view(), name="animal_detail"),   # 👈 detalle
    path("animales/<int:pk>/editar/", views_clases.AnimalUpdateView.as_view(), name="animal_update"),  # 👈 edición
    path("animales/<int:pk>/eliminar/", views_clases.AnimalDeleteView.as_view(), name="animal_delete"), # 👈 eliminación
]"""