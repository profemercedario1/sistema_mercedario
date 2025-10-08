from django.contrib import admin
from .models import Estudiante

# Registrar el modelo para que aparezca en el panel admin
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nota1', 'nota2', 'nota3', 'promedio')
    search_fields = ('nombre',)
    list_filter = ('promedio',)

