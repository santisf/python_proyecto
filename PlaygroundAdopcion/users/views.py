
from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.urls import reverse

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
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse('inicio'))
    else:
        form = UserEditForm(instance=usuario)

    return render(request, 'users/editar_usuario.html', {'form': form})


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

