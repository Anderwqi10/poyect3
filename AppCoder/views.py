from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *


def inicio(request):
      return render(request, "AppCoder/inicio.html")

# Agregar Datps

def cursos(request):
      if request.method == 'POST':
            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 
                  curso.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= CursoFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})


def estudiantes(request):
      if request.method == 'POST':
            miFormulario = EstudianteFormulario(request.POST) #aquí me llega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= EstudianteFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})


def profesores(request):
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion']) 
                  profesor.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})





# Busqueda

def buscar(request):
      if  request.GET["camada"]:
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)
            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
      else: 
            respuesta = "No enviaste datos"
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

def buscarProfesor(request):
      if  request.GET["profesion"]:
            profesion = request.GET['profesion'] 
            profesores = Profesor.objects.filter(profesion__icontains=profesion)
            return render(request, "AppCoder/inicio.html", {"profesores": profesores, "profesion":profesion})
      else: 
            respuesta = "No enviaste datos"
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

def buscarEstudiante(request):
      if  request.GET["nombre"]:
            nombre = request.GET['nombre'] 
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
            return render(request, "AppCoder/inicio.html", {"estudiantes": estudiantes, "nombre":nombre})
      else: 
            respuesta = "No enviaste datos"
      return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})

