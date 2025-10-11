from django.contrib.auth import get_user_model

User = get_user_model()
username = "roman"
password = "Roman678/*"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="", password=password)
    print(f"✅ Superusuario '{username}' creado correctamente.")
else:
    print(f"ℹ️ El usuario '{username}' ya existe.")
