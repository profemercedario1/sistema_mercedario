# usuarios_db.py
import sqlite3
import os
import hashlib
import secrets
from datetime import datetime

DB_PATH = "registros.db"
ITERACIONES = 120_000  # PBKDF2 (fuerte y razonable)

def _get_conn():
    return sqlite3.connect(DB_PATH)

def crear_tabla_usuarios():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def _hash_password(password: str, salt_hex: str) -> str:
    # password: str -> bytes
    salt = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        ITERACIONES
    )
    return dk.hex()

def crear_usuario(username: str, password: str, role: str = "docente") -> bool:
    """
    Crea un usuario nuevo.
    Retorna True si lo crea; False si el usuario ya existía.
    """
    username = username.strip().lower()
    if not username or not password:
        raise ValueError("Usuario y contraseña no pueden estar vacíos.")

    crear_tabla_usuarios()

    # Evitar duplicados
    if existe_usuario(username):
        return False

    salt_hex = secrets.token_hex(16)
    phash = _hash_password(password, salt_hex)
    now = datetime.now().isoformat(timespec="seconds")

    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO usuarios (username, password_hash, salt, role, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (username, phash, salt_hex, role, now))
    conn.commit()
    conn.close()
    return True

def existe_usuario(username: str) -> bool:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM usuarios WHERE username = ?", (username.strip().lower(),))
    row = cur.fetchone()
    conn.close()
    return row is not None

def verificar_usuario(username: str, password: str):
    """
    Verifica credenciales.
    Retorna (True, role) si son válidas. Si no, (False, None).
    """
    username = username.strip().lower()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT password_hash, salt, role FROM usuarios WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return False, None

    password_hash_db, salt_hex, role = row
    intento = _hash_password(password, salt_hex)
    if secrets.compare_digest(intento, password_hash_db):
        return True, role
    return False, None

def cambiar_password(username: str, new_password: str) -> bool:
    if not existe_usuario(username):
        return False
    salt_hex = secrets.token_hex(16)
    phash = _hash_password(new_password, salt_hex)
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE usuarios SET password_hash = ?, salt = ? WHERE username = ?
    """, (phash, salt_hex, username.strip().lower()))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok

def eliminar_usuario(username: str) -> bool:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE username = ?", (username.strip().lower(),))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok

def listar_usuarios():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, username, role, created_at FROM usuarios ORDER BY username")
    data = cur.fetchall()
    conn.close()
    return data

def asegurar_admin_inicial():
    """
    Crea un admin por defecto si no existe.
    Usuario: admin | Contraseña: 1234
    ⚠️ Recomendado cambiar luego con cambiar_password().
    """
    crear_tabla_usuarios()
    if not existe_usuario("admin"):
        crear_usuario("admin", "1234", role="admin")
