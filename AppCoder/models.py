from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Profesion: {self.profesion}"
    
