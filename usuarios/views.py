from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"👋 Bienvenido, {user.username}")
            return redirect('/')
        else:
            messages.error(request, "❌ Usuario o contraseña incorrectos")
    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "👋 Has cerrado sesión correctamente")
    return redirect("/login/")

