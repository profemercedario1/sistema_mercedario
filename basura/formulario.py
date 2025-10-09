from base_datos import insertar_estudiante

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def formulario():
    print("\n🧾 INGRESO DE ESTUDIANTE")
    nombre = input("Nombre: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    promedio = calcular_promedio(n1, n2, n3)
    insertar_estudiante(nombre, n1, n2, n3, promedio)
    print(f"✅ {nombre} registrado con promedio {promedio:.2f}\n")
