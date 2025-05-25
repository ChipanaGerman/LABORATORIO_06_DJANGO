from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio_app'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
     path('notas/', views.lista_notas, name='lista_notas'),
    path('notas/ingresar/', views.ingresar_nota, name='ingresar_nota'),
    path('notas/editar/<int:nota_id>/', views.editar_nota, name='editar_nota'), 
    path('notas/eliminar/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'), 
]
