from django import forms
from .models import NotasAlumnosPorCurso, Alumno, Curso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombres', 'apellidos', 'codigo_estudiante', 'email']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'codigo_curso', 'creditos']
class NotaForm(forms.ModelForm):

    class Meta:
        model = NotasAlumnosPorCurso
        fields = ['alumno', 'curso', 'nota'] 