from django.urls import path
from . import views

urlpatterns = [
    # 🔹 Página principal para registrar y listar estudiantes
    path('registrar/', views.registrar_estudiante, name='registrar_estudiante'),

    # 🔹 Rutas para editar y eliminar (si ya existen)
    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
]
