from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Estudiante
from .forms import EstudianteForm

@login_required(login_url='/login/')
def registrar_estudiante(request):
    # 🔹 Si se envía el formulario (POST)
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Estudiante registrado correctamente.')
            return redirect('registrar_estudiante')
        else:
            messages.error(request, '⚠️ Error al registrar el estudiante.')
    else:
        form = EstudianteForm()

    # 🔹 Obtener todos los estudiantes (ordenados del más reciente)
    lista_estudiantes = Estudiante.objects.all().order_by('-id')

    # 🔹 Paginación (10 registros por página)
    paginator = Paginator(lista_estudiantes, 10)
    page_number = request.GET.get('page')
    estudiantes = paginator.get_page(page_number)

    return render(request, 'estudiantes/registrar_estudiante.html', {
        'form': form,
        'estudiantes': estudiantes,
    })



@login_required(login_url='/login/')
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
        # 🔁 Redirigimos al formulario principal (no a '/')
        return redirect('registrar_estudiante')
    return render(request, 'estudiantes/editar_estudiante.html', {'estudiante': estudiante})


@login_required(login_url='/login/')
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    messages.warning(request, f"🗑️ {estudiante.nombre} fue eliminado.")
    # 🔁 Redirigimos también a la página de registro
    return redirect('registrar_estudiante')
