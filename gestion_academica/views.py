from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlumnoForm, CursoForm
from .models import Alumno, Curso
from .models import NotasAlumnosPorCurso 
from .forms import NotaForm 

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'gestion_academica/crear_alumno.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion_academica/lista_alumnos.html', {'alumnos': alumnos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion_academica/crear_curso.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_academica/lista_cursos.html', {'cursos': cursos})

def ingresar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('lista_notas') 
            except Exception as e: 
                form.add_error(None, f"Error al guardar: Es posible que ya exista una nota para este alumno en este curso. ({e})")

    else:
        form = NotaForm()
    return render(request, 'gestion_academica/ingresar_nota.html', {'form': form})

def lista_notas(request):
    notas = NotasAlumnosPorCurso.objects.all().order_by('-fecha_registro', 'alumno__apellidos', 'alumno__nombres')
    return render(request, 'gestion_academica/lista_notas.html', {'notas': notas})

def editar_nota(request, nota_id):
    nota_obj = get_object_or_404(NotasAlumnosPorCurso, id=nota_id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota_obj)
    return render(request, 'gestion_academica/editar_nota.html', {'form': form, 'nota_obj': nota_obj})

def eliminar_nota(request, nota_id):
    nota_obj = get_object_or_404(NotasAlumnosPorCurso, id=nota_id)
    if request.method == 'POST': 
        nota_obj.delete()
        return redirect('lista_notas')
    return render(request, 'gestion_academica/confirmar_eliminar_nota.html', {'nota_obj': nota_obj})

def pagina_inicio(request):
    context = {
        'titulo': "Bienvenido al Sistema de Gestión Académica",
    }
    return render(request, 'gestion_academica/pagina_inicio.html', context)


