from django.db import models

class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    codigo_curso = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_curso
