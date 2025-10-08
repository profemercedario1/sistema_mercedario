from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Estudiante
from .forms import EstudianteForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')  # 👈 solo usuarios autenticados podrán ver esta página
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes})

@login_required(login_url='/login/')
def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante registrado correctamente.')
            return redirect('/')  # ✅ ahora sí funcionará
        else:
            messages.error(request, 'Error al registrar el estudiante.')
    else:
        form = EstudianteForm()

    return render(request, 'estudiantes/registrar_estudiante.html', {'form': form})

@login_required(login_url='/login/')  # 👈 solo usuarios autenticados podrán ver esta página
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.nota1 = float(request.POST['nota1'])
        estudiante.nota2 = float(request.POST['nota2'])
        estudiante.nota3 = float(request.POST['nota3'])
        estudiante.promedio = round((estudiante.nota1 + estudiante.nota2 + estudiante.nota3) / 3, 2)
        estudiante.save()
        messages.info(request, f"✏️ {estudiante.nombre} fue actualizado con éxito.")
        return redirect('/')
    return render(request, 'estudiantes/editar_estudiante.html', {'estudiante': estudiante})

@login_required(login_url='/login/')  # 👈 solo usuarios autenticados podrán ver esta página
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    messages.warning(request, f"🗑️ {estudiante.nombre} fue eliminado.")
    return redirect('/')
