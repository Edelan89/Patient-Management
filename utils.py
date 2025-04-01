import os
import shutil
import tkinter as tk
from tkinter import filedialog


CARPETA_ARCHIVOS = os.path.join(os.path.expanduser(
    "~"), "Documents", "GestionPacientes", "archivos_pacientes")  # Carpeta en "Mis Documentos"

if not os.path.exists(CARPETA_ARCHIVOS):
    os.makedirs(CARPETA_ARCHIVOS)


def copiar_archivos(entries):
    fotos = entries['Fotos'].get()
    videos = entries['Videos'].get()

    if fotos:
        for foto in fotos.split(';'):
            if foto:
                nombre_foto = os.path.basename(foto)
                shutil.copy(foto, os.path.join(CARPETA_ARCHIVOS, nombre_foto))
                entries['Fotos'].delete(0, tk.END)
                entries['Fotos'].insert(tk.END, os.path.join(
                    CARPETA_ARCHIVOS, nombre_foto))

    if videos:
        for video in videos.split(';'):
            if video:
                nombre_video = os.path.basename(video)
                shutil.copy(video, os.path.join(
                    CARPETA_ARCHIVOS, nombre_video))
                entries['Videos'].delete(0, tk.END)
                entries['Videos'].insert(tk.END, os.path.join(
                    CARPETA_ARCHIVOS, nombre_video))


def copiar_archivos_pdf(entries):
    pdfs = entries['PDFs'].get()

    if pdfs:
        for pdf in pdfs.split(';'):
            if pdf:  # Asegurarse que no sea una cadena vacía
                nombre_pdf = os.path.basename(pdf)
                shutil.copy(pdf, os.path.join(CARPETA_ARCHIVOS, nombre_pdf))
                entries['PDFs'].delete(0, tk.END)  # Limpiar el campo
                entries['PDFs'].insert(tk.END, os.path.join(
                    CARPETA_ARCHIVOS, nombre_pdf))


def seleccionar_archivos_pdf(entry):
    archivos = filedialog.askopenfilenames(
        title='Seleccionar PDF', filetypes=[("Archivos PDF", "*.pdf")])
    if archivos:
        entry.delete(0, tk.END)
        entry.insert(tk.END, ';'.join(archivos))


def seleccionar_archivos(entry, tipo):
    archivos = filedialog.askopenfilenames(title=f'Seleccionar {tipo}', filetypes=[
                                           ("Todos los archivos", "*.*")])
    if archivos:
        entry.delete(0, tk.END)
        entry.insert(tk.END, ';'.join(archivos))


def limpiar_campos(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)
