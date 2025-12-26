
from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PerfilForm, AvatarForm
from .models import Avatar
from django.contrib import messages
"""
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                msg_login = f"Bienvenido {usuario}"
            else:
                msg_login = "Error, datos incorrectos"
        else:
            msg_login = "Error, formulario erróneo"
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})"""



@login_required
def editar_perfil(request):
    usuario = request.user
    # Asegurar que exista el Avatar asociado
    avatar, _ = Avatar.objects.get_or_create(user=usuario)

    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, instance=usuario)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if perfil_form.is_valid() and avatar_form.is_valid():
            perfil_form.save()
            avatar_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            # Redirigir al mismo formulario de edición (PRG) para que el mensaje
            # se muestre solo en la siguiente GET de esta misma URL
            return redirect(reverse('users:editar_perfil'))
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        perfil_form = PerfilForm(instance=usuario)
        avatar_form = AvatarForm(instance=avatar)

    return render(request, 'users/editar_usuario.html', {
        'perfil_form': perfil_form,
        'avatar_form': avatar_form,
    })





def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('inicio')   
        else:
            msg_login = "Error, formulario erróneo o credenciales inválidas"
    else:
        form = AuthenticationForm()
    form.fields["username"].label="Usuario    "
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppAdopcion/inicio.html", {"mensaje": "Usuario Creado :)"})
        msg_register = "Error en los datos ingresados"
    else:
        form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})



from django.contrib import messages

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy('users:editar_pass_done')

    def form_valid(self, form):
        messages.success(self.request, "Contraseña cambiada correctamente.")
        return super().form_valid(form)



