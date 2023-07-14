from django.shortcuts import render, redirect
from .models import Materia
from django.contrib import messages

# Create your views here.


def home(request):
    materias = Materia.objects.all()
    messages.success(request, '!Cursos Listados!')
    return render(request, "gestionCursos.html", {"materias": materias})


def registrarMateria(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    materia = Materia.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '!Curso Registrado!')
    return redirect('/')


def edicionMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    return render(request, "edicionMateria.html", {"materia": materia})


def editarMateria(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    materia = Materia.objects.get(codigo=codigo)
    materia.nombre = nombre
    materia.creditos = creditos
    materia.save()

    messages.success(request, '!Curso actualizado!')
    return redirect('/')


def eliminarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    materia.delete()
    messages.success(request, '!Curso eliminado!')
    return redirect('/')