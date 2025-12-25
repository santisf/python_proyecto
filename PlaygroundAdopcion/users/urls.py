from django.urls import path, include
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from . import views
from django.contrib.auth import views as auth_views

app_name = "users" # <- obligatorio para usar users:login
urlpatterns = [
    path('registro/', views.register, name='registro'),
    path('login/', views.login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('', include('django.contrib.auth.urls')),
]





