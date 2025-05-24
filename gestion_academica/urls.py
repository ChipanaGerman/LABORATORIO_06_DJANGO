from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
]
