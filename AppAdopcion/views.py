from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso


def inicio(request):
    return render (request , "AppCoder/inicio.html")

def cursos(request):
    lista_curso = Curso.objects.all()
    return render(request,"AppCoder/cursos.html",{"cursos":lista_curso})

def profesores(request):
     return render(request,"AppCoder/profesores.html")

def estudiantes(request):
     return render(request,"AppCoder/estudiantes.html")

def entregables(request):
     return render(request,"AppCoder/entregables.html")
