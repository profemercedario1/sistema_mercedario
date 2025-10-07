# ventana_login.py
import tkinter as tk
from tkinter import messagebox
import ventana_principal
import usuarios_db  # <-- NUEVO

def validar_login(event=None):
    usuario = entry_usuario.get().strip()
    clave = entry_clave.get().strip()

    # verificar contra SQLite
    ok, role = usuarios_db.verificar_usuario(usuario, clave)
    if ok:
        messagebox.showinfo("Acceso permitido", f"✅ Bienvenido, {usuario} ({role}).")
        root.destroy()
        # Pasa el usuario y rol a la ventana principal (opcional pero útil)
        ventana_principal.mostrar_ventana_principal(usuario, role)
    else:
        messagebox.showerror("Acceso denegado", "❌ Usuario o contraseña incorrectos.")
        entry_clave.delete(0, tk.END)
        entry_clave.focus()

# ---------- UI igual que ya tienes (con navegacion Enter/flechas) ----------
root = tk.Tk()
root.title("Acceso al Sistema - Unidad Educativa Maria de la Merced")
root.geometry("420x320")
root.resizable(False, False)
root.configure(bg="#f0f8ff")

# Asegura tabla y un admin por defecto
usuarios_db.asegurar_admin_inicial()

tk.Label(root, text="UNIDAD EDUCATIVA\nMARIA DE LA MERCED",
         bg="#f0f8ff", fg="#003366", font=("Arial", 14, "bold")).pack(pady=20)

frame = tk.Frame(root, bg="#f0f8ff"); frame.pack(pady=10)

tk.Label(frame, text="Usuario:", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=8, sticky="e")
entry_usuario = tk.Entry(frame, width=25); entry_usuario.grid(row=0, column=1, padx=5, pady=8)

tk.Label(frame, text="Contraseña:", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=8, sticky="e")
entry_clave = tk.Entry(frame, show="*", width=25); entry_clave.grid(row=1, column=1, padx=5, pady=8)

# Navegación
def focus_siguiente(event, siguiente): siguiente.focus(); return "break"
def focus_anterior(event, anterior): anterior.focus(); return "break"

entry_usuario.bind("<Return>", lambda e: focus_siguiente(e, entry_clave))
entry_clave.bind("<Return>", validar_login)
entry_usuario.bind("<Down>", lambda e: focus_siguiente(e, entry_clave))
entry_clave.bind("<Up>", lambda e: focus_anterior(e, entry_usuario))

tk.Button(root, text="🔐 Ingresar", bg="#003366", fg="white",
          font=("Arial", 11, "bold"), width=15, command=validar_login).pack(pady=20)

tk.Label(root, text="PERIODO LECTIVO 2025 - 2026",
         bg="#f0f8ff", fg="#333333", font=("Arial", 9, "italic")).pack(side="bottom", pady=10)

entry_usuario.focus()
root.mainloop()
