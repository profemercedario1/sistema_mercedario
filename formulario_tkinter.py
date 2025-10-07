import tkinter as tk
from tkinter import messagebox, PhotoImage
from base_datos import insertar_estudiante
from reporte_pdf import generar_pdf
import os

# =====================================================
# FUNCIONES LÓGICAS
# =====================================================

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def guardar(entry_nombre, entry_n1, entry_n2, entry_n3):
    nombre = entry_nombre.get().strip()
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        n3 = float(entry_n3.get())
    except ValueError:
        messagebox.showerror("Error", "❌ Las notas deben ser numéricas.")
        return

    if not nombre:
        messagebox.showwarning("Atención", "⚠️ El nombre no puede estar vacío.")
        return

    promedio = calcular_promedio(n1, n2, n3)
    insertar_estudiante(nombre, n1, n2, n3, promedio)
    messagebox.showinfo("Registro exitoso", f"✅ {nombre} registrado con promedio {promedio:.2f}")

    limpiar_campos(entry_nombre, entry_n1, entry_n2, entry_n3)

def limpiar_campos(entry_nombre, entry_n1, entry_n2, entry_n3):
    entry_nombre.delete(0, tk.END)
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    entry_n3.delete(0, tk.END)
    entry_nombre.focus()

# =====================================================
# FUNCIÓN PARA GENERAR Y ABRIR PDF
# =====================================================

def generar_y_abrir_pdf():
    try:
        generar_pdf()
        messagebox.showinfo("Reporte generado", "📄 El reporte PDF se ha creado correctamente.")
        if os.path.exists("reporte_estudiantes.pdf"):
            os.startfile("reporte_estudiantes.pdf")  # Solo funciona en Windows
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema al generar el PDF:\n{e}")

# =====================================================
# FUNCIÓN PRINCIPAL PARA MOSTRAR EL FORMULARIO
# =====================================================

def mostrar_formulario():
    ventana = tk.Toplevel()
    ventana.title("Formulario de Ingreso - Unidad Educativa Maria de la Merced")
    ventana.geometry("420x580")
    ventana.resizable(False, False)
    ventana.configure(bg="#f0f8ff")

    # Título
    tk.Label(
        ventana,
        text="UNIDAD EDUCATIVA MARIA DE LA MERCED",
        bg="#f0f8ff",
        fg="#003366",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    frame = tk.Frame(ventana, bg="#f0f8ff")
    frame.pack(pady=5)

    # Campos
    tk.Label(frame, text="Nombre:", bg="#f0f8ff", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_nombre = tk.Entry(frame, width=30)
    entry_nombre.grid(row=0, column=1)

    tk.Label(frame, text="Nota 1:", bg="#f0f8ff", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_n1 = tk.Entry(frame, width=10)
    entry_n1.grid(row=1, column=1, sticky="w")

    tk.Label(frame, text="Nota 2:", bg="#f0f8ff", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_n2 = tk.Entry(frame, width=10)
    entry_n2.grid(row=2, column=1, sticky="w")

    tk.Label(frame, text="Nota 3:", bg="#f0f8ff", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_n3 = tk.Entry(frame, width=10)
    entry_n3.grid(row=3, column=1, sticky="w")

    # =====================================================
    # NAVEGACIÓN CON ENTER Y FLECHAS
    # =====================================================

    def focus_siguiente(event, siguiente):
        siguiente.focus()
        return "break"

    def focus_anterior(event, anterior):
        anterior.focus()
        return "break"

    entry_nombre.bind("<Return>", lambda e: focus_siguiente(e, entry_n1))
    entry_n1.bind("<Return>", lambda e: focus_siguiente(e, entry_n2))
    entry_n2.bind("<Return>", lambda e: focus_siguiente(e, entry_n3))
    entry_n3.bind("<Return>", lambda e: guardar(entry_nombre, entry_n1, entry_n2, entry_n3))

    entry_nombre.bind("<Down>", lambda e: focus_siguiente(e, entry_n1))
    entry_n1.bind("<Down>", lambda e: focus_siguiente(e, entry_n2))
    entry_n2.bind("<Down>", lambda e: focus_siguiente(e, entry_n3))

    entry_n3.bind("<Up>", lambda e: focus_anterior(e, entry_n2))
    entry_n2.bind("<Up>", lambda e: focus_anterior(e, entry_n1))
    entry_n1.bind("<Up>", lambda e: focus_anterior(e, entry_nombre))

    # =====================================================
    # BOTONES DE ACCIÓN
    # =====================================================

    tk.Button(
        ventana,
        text="💾 Guardar Estudiante",
        bg="#003366",
        fg="white",
        font=("Arial", 10, "bold"),
        width=22,
        command=lambda: guardar(entry_nombre, entry_n1, entry_n2, entry_n3)
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="📄 Generar y Ver Reporte PDF",
        bg="#006633",
        fg="white",
        font=("Arial", 10, "bold"),
        width=22,
        command=generar_y_abrir_pdf
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="🚪 Cerrar",
        bg="#cc0000",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10,
        command=ventana.destroy
    ).pack(pady=10)

    # =====================================================
    # ESCUDO Y PIE DE PÁGINA
    # =====================================================

    try:
        escudo = PhotoImage(file="escudo_mercedario.png")
        label_escudo = tk.Label(ventana, image=escudo, bg="#f0f8ff")
        label_escudo.pack(pady=10)
        ventana.escudo_ref = escudo  # evitar que se borre la imagen
    except Exception as e:
        print("⚠️ No se pudo cargar la imagen del escudo:", e)

    tk.Label(
        ventana,
        text="PERIODO LECTIVO 2025 - 2026",
        bg="#f0f8ff",
        fg="#333333",
        font=("Arial", 10, "italic")
    ).pack(pady=10)

    entry_nombre.focus()

# =====================================================
# NO INICIAR AUTOMÁTICAMENTE AL IMPORTAR
# =====================================================

if __name__ == "__main__":
    mostrar_formulario()
