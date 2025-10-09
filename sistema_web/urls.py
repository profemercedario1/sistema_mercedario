"""
URL configuration for sistema_web project.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from usuarios import views  # 👈 vistas de login/logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Si alguien entra a la raíz (/), lo redirigimos automáticamente al formulario
    path('', lambda request: redirect('registrar_estudiante')),

    # ✅ Incluimos todas las rutas de la app 'estudiantes'
    path('', include('estudiantes.urls')),

    # ✅ Rutas de login y logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]





