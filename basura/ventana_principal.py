import tkinter as tk
from tkinter import messagebox
from formulario_tkinter import mostrar_formulario
from reporte_pdf import generar_pdf
import os

# Si existe la ventana de administración de usuarios, la importamos
try:
    from ventana_admin_usuarios import abrir_admin_usuarios
except ImportError:
    abrir_admin_usuarios = None  # si no existe, se ignora sin error


# =====================================================
# FUNCIÓN PRINCIPAL - MENÚ DEL SISTEMA
# =====================================================

def mostrar_ventana_principal(usuario="(desconocido)", role="docente"):
    root = tk.Tk()
    root.title(f"Sistema Académico - {usuario} [{role}] - Unidad Educativa Maria de la Merced")
    root.configure(bg="#e6f0ff")
    root.resizable(True, True)

    # === Maximizar ventana al iniciar ===
    try:
        root.state('zoomed')  # Windows / Linux
    except:
        root.attributes('-zoomed', True)  # macOS

    # ----------------------------
    # BARRA DE MENÚ
    # ----------------------------
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu)

    # --- Menú "Archivo"
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    menu_archivo.add_command(label="Cerrar sesión", command=root.destroy)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir del sistema", command=root.quit)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    # --- Menú "Gestión"
    menu_gestion = tk.Menu(barra_menu, tearoff=0)
    menu_gestion.add_command(label="📋 Ingresar Estudiantes", command=abrir_formulario)
    menu_gestion.add_command(label="📄 Generar Reporte PDF", command=abrir_pdf)

    # Si el usuario es administrador, muestra el submenú de usuarios
    if role.lower() == "admin" and abrir_admin_usuarios:
        menu_gestion.add_separator()
        menu_gestion.add_command(label="👥 Administración de Usuarios", command=abrir_admin_usuarios)

    barra_menu.add_cascade(label="Gestión", menu=menu_gestion)

    # --- Menú "Ayuda"
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="Acerca de...", command=mostrar_info)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    # ----------------------------
    # ENCABEZADO Y DISEÑO
    # ----------------------------
    tk.Label(
        root,
        text="UNIDAD EDUCATIVA MARIA DE LA MERCED",
        bg="#e6f0ff",
        fg="#003366",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    try:
        escudo = tk.PhotoImage(file="escudo_mercedario.png")
        label_escudo = tk.Label(root, image=escudo, bg="#e6f0ff")
        label_escudo.pack(pady=10)
        root.escudo_ref = escudo  # evita que se elimine la imagen
    except Exception as e:
        print("⚠️ No se pudo cargar el escudo:", e)

    tk.Label(
        root,
        text="SISTEMA DE GESTIÓN ACADÉMICA",
        bg="#e6f0ff",
        fg="#004080",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # ----------------------------
    # BOTONES PRINCIPALES
    # ----------------------------
    frame_botones = tk.Frame(root, bg="#e6f0ff")
    frame_botones.pack(pady=50)

    boton_ingresar = tk.Button(
        frame_botones,
        text="📋 Ingresar Estudiantes",
        bg="#003366",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        command=abrir_formulario
    )
    boton_ingresar.grid(row=0, column=0, padx=40, pady=20)

    boton_pdf = tk.Button(
        frame_botones,
        text="📄 Generar Reporte PDF",
        bg="#006633",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        command=abrir_pdf
    )
    boton_pdf.grid(row=0, column=1, padx=40, pady=20)

    # Solo mostrar el botón de administración si el usuario es admin
    if role.lower() == "admin" and abrir_admin_usuarios:
        boton_admin = tk.Button(
            frame_botones,
            text="👥 Administrar Usuarios",
            bg="#004d66",
            fg="white",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            command=abrir_admin_usuarios
        )
        boton_admin.grid(row=1, column=0, columnspan=2, pady=15)

    boton_salir = tk.Button(
        frame_botones,
        text="🚪 Cerrar Sesión",
        bg="#cc0000",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        command=root.destroy
    )
    boton_salir.grid(row=2, column=0, columnspan=2, pady=25)

    # ----------------------------
    # PIE DE PÁGINA
    # ----------------------------
    tk.Label(
        root,
        text="PERIODO LECTIVO 2025 - 2026",
        bg="#e6f0ff",
        fg="#333333",
        font=("Arial", 11, "italic")
    ).pack(side="bottom", pady=20)

    root.mainloop()

# =====================================================
# FUNCIONES AUXILIARES
# =====================================================

def abrir_formulario():
    """Abre el formulario de ingreso en una nueva ventana."""
    mostrar_formulario()

def abrir_pdf():
    """Genera y abre el PDF directamente."""
    try:
        generar_pdf()
        if os.path.exists("reporte_estudiantes.pdf"):
            os.startfile("reporte_estudiantes.pdf")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el PDF:\n{e}")

def mostrar_info():
    messagebox.showinfo(
        "Acerca de",
        "Sistema Académico - Unidad Educativa Maria de la Merced\nVersión 1.0\nDesarrollado en Python con Tkinter"
    )

# =====================================================
# EJECUCIÓN DIRECTA (para pruebas)
# =====================================================
if __name__ == "__main__":
    mostrar_ventana_principal(usuario="admin", role="admin")
