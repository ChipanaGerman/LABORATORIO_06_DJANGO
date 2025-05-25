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
class NotasAlumnosPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='notas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='notas_en_curso')
    nota = models.DecimalField(max_digits=4, decimal_places=2) 
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Meta:
        unique_together = ('alumno', 'curso')
        verbose_name = "Nota por Curso"
        verbose_name_plural = "Notas por Curso"

def __str__(self):
        return f"Nota de {self.alumno} en {self.curso}: {self.nota}"
