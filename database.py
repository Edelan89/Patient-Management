import sqlite3
import os

# Define la ubicación de la base de datos en la carpeta "Mis Documentos"
BASE_DIR = os.path.expanduser("~")  # Carpeta del usuario
DB_PATH = os.path.join(BASE_DIR, "Documents",
                       "GestionPacientes", "pacientes.db")


def crear_base_datos():
    # Crea la carpeta si no existe
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        edad TEXT,
        telefono TEXT,
        email TEXT,
        diagnostico TEXT,
        evolucion TEXT,
        tratamiento TEXT,
        fotos TEXT,
        videos TEXT,
        pdfs TEXT
    )
    """)
    conexion.commit()
    conexion.close()


def guardar_paciente(datos):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO pacientes (nombre, apellido, edad, telefono, email, diagnostico, evolucion, tratamiento, fotos, videos, pdfs)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, datos)
    conexion.commit()
    conexion.close()


def buscar_paciente(nombre, apellido):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT * FROM pacientes WHERE LOWER(nombre) = LOWER(?) AND LOWER(apellido) = LOWER(?)', (nombre, apellido))
    paciente = cursor.fetchone()
    conexion.close()
    return paciente


def obtener_pacientes():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    conexion.close()
    return pacientes


def eliminar_paciente(id):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM pacientes WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()


def modificar_paciente(id, datos):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
    UPDATE pacientes SET
        nombre = ?,
        apellido = ?,
        edad = ?,
        telefono = ?,
        email = ?,
        diagnostico = ?,
        evolucion = ?,
        tratamiento = ?,
        fotos = ?,
        videos = ?,
        pdfs = ?
    WHERE id = ?
    """, (*datos, id))
    conexion.commit()
    conexion.close()
