from django.urls import path
from AppAdopcion import views_clases
from .views_clases import BuscarAnimalView, SolicitudCreateView, SolicitudUpdateView, SolicitudDeleteView
from users import views

urlpatterns = [
    
    path('', views_clases.InicioView.as_view(), name='inicio'),
    path('animales/', views_clases.AnimalListView.as_view(), name='animales_list'),
    path("animales/nuevo/", views_clases.AnimalCreateView.as_view(), name="animal_create"),
    path("adoptantes/nuevo/", views_clases.AdoptanteCreateView.as_view(), name="adoptante_create"),
    path("solicitudes/nuevo/", views_clases.SolicitudCreateView.as_view(), name="solicitud_create"),
    path('adoptantes/', views_clases.AdoptanteListView.as_view(), name='adoptantes_list'),
    path('solicitudes/', views_clases.SolicitudListView.as_view(), name='solicitudes_list'),
    path("buscar/", BuscarAnimalView.as_view(), name="buscar"),
    path('login/' , views.login_request, name = 'Login'),

    path("animales/<int:pk>/", views_clases.AnimalDetailView.as_view(), name="animal_detail"),   #  detalle
    path("animales/<int:pk>/editar/", views_clases.AnimalUpdateView.as_view(), name="animal_update"),  #  edición
    path("animales/<int:pk>/eliminar/", views_clases.AnimalDeleteView.as_view(), name="animal_delete"), # eliminación
    path('solicitudes/nuevo/', SolicitudCreateView.as_view(), name='solicitud_create'),
    path('solicitudes/nuevo/<int:animal_pk>/', SolicitudCreateView.as_view(), name='solicitud_create_with_animal'),
    path('solicitudes/<int:pk>/editar/', SolicitudUpdateView.as_view(), name='solicitud_update'),
    path('solicitudes/<int:pk>/eliminar/', SolicitudDeleteView.as_view(), name='solicitud_delete'),
]
 



