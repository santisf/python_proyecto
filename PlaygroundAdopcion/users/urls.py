from django.urls import path, include
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from . import views 
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = "users" # <- obligatorio para usar users:login
urlpatterns = [
    path('registro/', views.register, name='registro'),
    path('login/', views.login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar_pass/', views.PasswordChange.as_view(), name='editar_pass'),
    path('perfil/editar_pass/done/', TemplateView.as_view(template_name='users/editar_pass_done.html'), name='editar_pass_done'),
    path('', include('django.contrib.auth.urls')),
]




