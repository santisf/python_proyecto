from django.shortcuts import render
from AppAdopcion.models import Animal, Adoptante, Solicitud
from django.shortcuts import redirect
from .forms import AnimalForm, AdoptanteForm, SolicitudForm


def inicio(request):
    return render(request, "AppAdopcion/inicio.html")

def cursos(request):   # muestra animales (nombre de la función se mantiene)
    lista_animales = Animal.objects.all()
    return render(request, "AppAdopcion/animales.html", {"cursos": lista_animales})

def profesores(request):  # plantilla genérica / formulario
    return render(request, "AppAdopcion/animal_create.html")

def estudiantes(request):  # muestra adoptantes
    lista_adoptantes = Adoptante.objects.all()
    return render(request, "AppAdopcion/adoptantes.html", {"adoptantes": lista_adoptantes})

def entregables(request):  # muestra solicitudes
    lista_solicitudes = Solicitud.objects.all()
    return render(request, "AppAdopcion/solicitudes.html", {"solicitudes": lista_solicitudes})

def buscar(request):
    q = request.GET.get('q', '').strip()
    resultados = []
    if q:
        resultados = Animal.objects.filter(nombre__icontains=q)
    return render(request, "AppAdopcion/buscar.html", {"query": q, "resultados": resultados})


def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animales_list')
    else:
        form = AnimalForm()
    return render(request, "AppAdopcion/animal_create.html", {"form": form})

def adoptante_create(request):
    if request.method == 'POST':
        form = AdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoptantes_list')
    else:
        form = AdoptanteForm()
    return render(request, "AppAdopcion/adoptante_create.html", {"form": form})

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitudes_list')
    else:
        form = SolicitudForm()
    return render(request, "AppAdopcion/solicitud_create.html", {"form": form})