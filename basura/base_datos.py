import sqlite3

def crear_tabla():
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL,
            nota3 REAL NOT NULL,
            promedio REAL
        )
    """)
    conn.commit()
    conn.close()

def insertar_estudiante(nombre, n1, n2, n3, promedio):
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (nombre, nota1, nota2, nota3, promedio)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, n1, n2, n3, promedio))
    conn.commit()
    conn.close()

def listar_estudiantes():
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    registros = cursor.fetchall()
    conn.close()
    return registros
