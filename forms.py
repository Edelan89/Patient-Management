import tkinter as tk
import shutil
import os
from tkinter import messagebox, ttk
from utils import copiar_archivos, seleccionar_archivos, limpiar_campos, copiar_archivos_pdf, seleccionar_archivos_pdf
from database import guardar_paciente, buscar_paciente, eliminar_paciente, modificar_paciente

# Define la carpeta para guardar archivos, si no existe la crea
CARPETA_ARCHIVOS = os.path.join(os.path.expanduser(
    "~"), "Documents", "GestionPacientes", "archivos_pacientes")  # Carpeta en "Mis Documentos"

if not os.path.exists(CARPETA_ARCHIVOS):
    os.makedirs(CARPETA_ARCHIVOS)


def ventana_agregar_paciente(callback=None):
    formulario = tk.Toplevel()
    formulario.title("Agregar Paciente")

    campos = ['Nombre', 'Apellido', 'Edad', 'Telefono', 'Email',
              'Diagnostico', 'Evolucion', 'Tratamiento', 'Fotos', 'Videos', 'PDFs']

    entries = {}

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo).grid(
            row=i, column=0, padx=10, pady=10)
        entry = tk.Entry(formulario)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[campo] = entry

        if campo in ['Fotos', 'Videos', 'PDFs']:
            frame = tk.Frame(formulario)
            frame.grid(row=i, column=2, padx=10, pady=10)
            if campo == 'PDFs':
                btn_seleccionar = ttk.Button(
                    frame, text="Seleccionar", command=lambda entry=entry: seleccionar_archivos_pdf(entry))
            else:
                btn_seleccionar = ttk.Button(
                    frame, text="Seleccionar", command=lambda entry=entry, tipo=campo: seleccionar_archivos(entry, tipo))
            btn_seleccionar.pack(side=tk.LEFT)

    def guardar_paciente_form():
        nombre = entries['Nombre'].get()
        apellido = entries['Apellido'].get()
        edad = entries['Edad'].get()
        telefono = entries['Telefono'].get()
        email = entries['Email'].get()
        diagnostico = entries['Diagnostico'].get()
        evolucion = entries['Evolucion'].get()
        tratamiento = entries['Tratamiento'].get()
        fotos = entries['Fotos'].get()
        videos = entries['Videos'].get()
        pdfs = entries['PDFs'].get()

        # Crear carpeta para el paciente
        carpeta_paciente = f"{nombre} {apellido}"
        ruta_carpeta_paciente = os.path.join(
            CARPETA_ARCHIVOS, carpeta_paciente)

        if not os.path.exists(ruta_carpeta_paciente):
            os.makedirs(ruta_carpeta_paciente)

        # Copiar archivos a la carpeta del paciente
        if fotos:
            for foto in fotos.split(';'):
                if foto:
                    nombre_foto = os.path.basename(foto)
                    shutil.copy(foto, os.path.join(
                        ruta_carpeta_paciente, nombre_foto))
                    entries['Fotos'].delete(0, tk.END)
                    entries['Fotos'].insert(tk.END, os.path.join(
                        ruta_carpeta_paciente, nombre_foto))

        if videos:
            for video in videos.split(';'):
                if video:
                    nombre_video = os.path.basename(video)
                    shutil.copy(video, os.path.join(
                        ruta_carpeta_paciente, nombre_video))
                    entries['Videos'].delete(0, tk.END)
                    entries['Videos'].insert(tk.END, os.path.join(
                        ruta_carpeta_paciente, nombre_video))

        if pdfs:
            for pdf in pdfs.split(';'):
                if pdf:
                    nombre_pdf = os.path.basename(pdf)
                    shutil.copy(pdf, os.path.join(
                        ruta_carpeta_paciente, nombre_pdf))
                    entries['PDFs'].delete(0, tk.END)
                    entries['PDFs'].insert(tk.END, os.path.join(
                        ruta_carpeta_paciente, nombre_pdf))

        # Guardar datos en la base de datos
        datos = (nombre, apellido, edad, telefono, email, diagnostico,
                 evolucion, tratamiento, fotos, videos, pdfs)
        guardar_paciente(datos)
        messagebox.showinfo("Paciente Agregado",
                            "Paciente agregado correctamente.")

        if callback:
            callback()

        limpiar_campos(entries)

    btn_guardar = ttk.Button(formulario, text="Guardar",
                             command=guardar_paciente_form)
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, pady=10)


def ventana_buscar_paciente():
    formulario = tk.Toplevel()
    formulario.title("Buscar Paciente")

    campos = ['Nombre', 'Apellido']
    entries = {}

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo).grid(
            row=i, column=0, padx=10, pady=10)
        entry = tk.Entry(formulario)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[campo] = entry

    def realizar_busqueda():
        nombre = entries['Nombre'].get()
        apellido = entries['Apellido'].get()

        if not nombre or not apellido:
            messagebox.showwarning(
                "Advertencia", "Los campos 'Nombre' y 'Apellido' son obligatorios")
            return

        paciente = buscar_paciente(nombre, apellido)
        if paciente:
            resultado_label.config(text=f"Nombre: {paciente[1]}\n"
                                        f"Apellido: {paciente[2]}\n"
                                        f"Edad: {paciente[3]}\n"
                                        f"Teléfono: {paciente[4]}\n"
                                        f"Email: {paciente[5]}\n"
                                        f"Diagnóstico: {paciente[6]}\n"
                                        f"Evolución: {paciente[7]}\n"
                                        f"Tratamiento: {paciente[8]}\n"
                                        f"Fotos: {paciente[9]}\n"
                                        f"Videos: {paciente[10]}\n"
                                        f"PDFs: {paciente[11]}")
        else:
            resultado_label.config(text="Paciente no encontrado.")

    btn_buscar = ttk.Button(formulario, text="Buscar",
                            command=realizar_busqueda)
    btn_buscar.grid(row=len(campos), column=0, columnspan=2, pady=10)

    resultado_label = tk.Label(formulario, text="", justify=tk.LEFT)
    resultado_label.grid(row=len(campos) + 1, column=0,
                         columnspan=2, padx=10, pady=10)


def ventana_mostrar_info_paciente(paciente):
    formulario = tk.Toplevel()
    formulario.title("Información del Paciente")

    tk.Label(formulario, text=f"Nombre: {paciente[1]}").pack()
    tk.Label(formulario, text=f"Apellido: {paciente[2]}").pack()
    tk.Label(formulario, text=f"Edad: {paciente[3]}").pack()
    tk.Label(formulario, text=f"Teléfono: {paciente[4]}").pack()
    tk.Label(formulario, text=f"Email: {paciente[5]}").pack()
    tk.Label(formulario, text=f"Diagnóstico: {paciente[6]}").pack()
    tk.Label(formulario, text=f"Evolución: {paciente[7]}").pack()
    tk.Label(formulario, text=f"Tratamiento: {paciente[8]}").pack()

    # Agregar botones para abrir archivos
    tk.Label(formulario, text="Fotos:").pack()
    fotos = paciente[9].split(';') if paciente[9] else []
    for foto in fotos:
        if foto:
            tk.Button(formulario, text=os.path.basename(foto),
                      command=lambda foto=foto: abrir_archivo(foto)).pack()

    tk.Label(formulario, text="Videos:").pack()
    videos = paciente[10].split(';') if paciente[10] else []
    for video in videos:
        if video:
            tk.Button(formulario, text=os.path.basename(video),
                      command=lambda video=video: abrir_archivo(video)).pack()

    tk.Label(formulario, text="PDFs:").pack()
    pdfs = paciente[11].split(';') if paciente[11] else []
    for pdf in pdfs:
        if pdf:
            tk.Button(formulario, text=os.path.basename(pdf),
                      command=lambda pdf=pdf: abrir_archivo(pdf)).pack()


def abrir_archivo(ruta):
    try:
        os.startfile(ruta)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")


def ventana_eliminar_paciente(callback=None):
    formulario = tk.Toplevel()
    formulario.title("Eliminar Paciente")

    campos = ['Nombre', 'Apellido']
    entries = {}

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo).grid(
            row=i, column=0, padx=10, pady=10)
        entry = tk.Entry(formulario)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[campo] = entry

    def eliminar_paciente_form():
        nombre = entries['Nombre'].get()
        apellido = entries['Apellido'].get()

        if not nombre or not apellido:
            messagebox.showwarning(
                "Advertencia", "Los campos 'Nombre' y 'Apellido' son obligatorios")
            return

        paciente = buscar_paciente(nombre, apellido)
        if paciente:
            eliminar_paciente(paciente[0])
            messagebox.showinfo("Paciente Eliminado",
                                "Paciente eliminado correctamente.")
            # Llamar al callback para actualizar el Listbox
            if callback:
                callback()
        else:
            messagebox.showerror("Error", "Paciente no encontrado.")

    btn_eliminar = ttk.Button(
        formulario, text="Eliminar", command=eliminar_paciente_form)
    btn_eliminar.grid(row=len(campos), column=0, columnspan=2, pady=10)


def ventana_modificar_paciente():
    formulario = tk.Toplevel()
    formulario.title("Modificar Paciente")

    tk.Label(formulario, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(formulario, text="Apellido").grid(
        row=1, column=0, padx=10, pady=10)

    nombre_entry = tk.Entry(formulario)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10)

    apellido_entry = tk.Entry(formulario)
    apellido_entry.grid(row=1, column=1, padx=10, pady=10)

    def buscar_paciente_modificar():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        paciente = buscar_paciente(nombre, apellido)
        if paciente:
            ventana_modificar_paciente_form(paciente)
        else:
            messagebox.showerror("Error", "Paciente no encontrado.")

    btn_buscar = ttk.Button(formulario, text="Buscar",
                            command=buscar_paciente_modificar)
    btn_buscar.grid(row=2, column=0, columnspan=2, pady=10)


def ventana_modificar_paciente_form(paciente):
    formulario = tk.Toplevel()
    formulario.title("Modificar Paciente")

    campos = ['Nombre', 'Apellido', 'Edad', 'Telefono', 'Email',
              'Diagnostico', 'Evolucion', 'Tratamiento', 'Fotos', 'Videos', 'PDFs']
    entries = {}

        #Mapeo de campos a indices en la tupla paciente
    campo_a_indice = {
        'Nombre': 1,
        'Apellido': 2,
        'Edad': 3,
        'Telefono': 4,
        'Email': 5,
        'Diagnostico': 6,
        'Evolucion': 7,
        'Tratamiento': 8,
        'Fotos': 9,
        'Videos': 10,
        'PDFs': 11
    }

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo).grid(
            row=i, column=0, padx=10, pady=10)

        entry = tk.Entry(formulario)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries[campo] = entry

        # Insertar valor previo en el campo, manejando None
        valor_previo = paciente[campo_a_indice[campo]] or ''
        entry.insert(tk.END, valor_previo)

        if campo in ['Fotos', 'Videos', 'PDFs']:
            frame = tk.Frame(formulario)
            frame.grid(row=i, column=2, padx=10, pady=10)

            # Botón para seleccionar archivos
            if campo == 'PDFs':
                btn_seleccionar = ttk.Button(
                    frame, text="Seleccionar", command=lambda entry=entry: seleccionar_archivos_pdf(entry))
            else:
                btn_seleccionar = ttk.Button(
                    frame, text="Seleccionar", command=lambda entry=entry, tipo=campo: seleccionar_archivos(entry, tipo))
            btn_seleccionar.pack(side=tk.LEFT)

            # Botón para mostrar y eliminar archivos existentes
            btn_gestionar = ttk.Button(
                frame, text="Gestionar", command=lambda campo=campo: gestionar_archivos(campo, paciente, entries[campo]))
            btn_gestionar.pack(side=tk.LEFT)

# Agregar botón para guardar cambios
    def guardar_cambios():
        datos = (
            entries['Nombre'].get(),
            entries['Apellido'].get(),
            entries['Edad'].get(),
            entries['Telefono'].get(),
            entries['Email'].get(),
            entries['Diagnostico'].get(),
            entries['Evolucion'].get(),
            entries['Tratamiento'].get(),
            entries['Fotos'].get(),
            entries['Videos'].get(),
            entries['PDFs'].get()
        )
        modificar_paciente(paciente[0], datos)
        messagebox.showinfo("Cambios Guardados", "Cambios guardados correctamente.")

        # Validar campos obligatorios
        if not entries['Nombre'].get() or not entries['Apellido'].get():
            messagebox.showwarning(
                "Advertencia", "Los campos 'Nombre' y 'Apellido' son obligatorios")
            return
        
    btn_guardar = ttk.Button(formulario, text="Guardar Cambios", command=guardar_cambios)
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, pady=10)

'''        # Llama a la función para guardar los archivos en una carpeta
        guardar_archivos_en_carpeta(nombre, apellido, fotos, videos, pdfs)

        datos = (nombre, apellido, edad, telefono, email, diagnostico,
                 evolucion, tratamiento, fotos, videos, pdfs)
        modificar_paciente(paciente[0], datos)
        messagebox.showinfo("Paciente Modificado",
                            "Paciente modificado correctamente.")'''

def gestionar_archivos(campo, paciente, entry_widget):
        # Obtiene la lista de archivos existente
        archivos_existente = getattr(paciente, campo.lower(), '') or ''
        lista_archivos = archivos_existente.split(';')

        ventana_gestionar = tk.Toplevel()
        ventana_gestionar.title(f"Gestionar {campo}")

        def eliminar_archivo(ruta):
            # Elimina la ruta del archivo de la lista
            lista_archivos.remove(ruta)
            # Actualiza la lista de archivos mostrada
            actualizar_lista_archivos()

        def actualizar_lista_archivos():
            # Limpia el frame
            for widget in frame_archivos.winfo_children():
                widget.destroy()

            # Agrega los archivos a la lista
            for archivo in lista_archivos:
                if archivo:
                    frame_archivo = tk.Frame(frame_archivos)
                    frame_archivo.pack(pady=5)

                    # Etiqueta con el nombre del archivo
                    lbl_archivo = tk.Label(
                        frame_archivo, text=os.path.basename(archivo))
                    lbl_archivo.pack(side=tk.LEFT)

                    # Botón para eliminar el archivo
                    btn_eliminar = ttk.Button(
                        frame_archivo, text="Eliminar", command=lambda archivo=archivo: eliminar_archivo(archivo))
                    btn_eliminar.pack(side=tk.LEFT)

            def confirmar_cambios():
                # Une la lista de archivos en una cadena separada por ;
                nueva_lista_archivos = ';'.join(lista_archivos)

                # Actualiza el campo correspondiente en el entry
                entry_widget.delete(0, tk.END)
                entry_widget.insert(tk.END, nueva_lista_archivos)

                # Actualiza el paciente en la base de datos
                datos = list(paciente)
                indice_campo = ['nombre', 'apellido', 'edad', 'telefono', 'email', 'diagnostico',
                                'evolucion', 'tratamiento', 'fotos', 'videos', 'pdfs'].index(campo.lower())
                datos[indice_campo + 1] = nueva_lista_archivos
                modificar_paciente(paciente[0], datos)

                # Cierra la ventana
                ventana_gestionar.destroy()

            frame_archivos = tk.Frame(ventana_gestionar)
            frame_archivos.pack(padx=10, pady=10)

            # Actualiza la lista de archivos mostrada
            actualizar_lista_archivos()

            # Botón para confirmar los cambios
            btn_confirmar = ttk.Button(
                ventana_gestionar, text="Confirmar", command=confirmar_cambios)
            btn_confirmar.pack(pady=10)


def guardar_archivos_en_carpeta(nombre, apellido, fotos, videos, pdfs):
    # Crear carpeta para el paciente
    carpeta_paciente = f"{nombre} {apellido}"
    ruta_carpeta_paciente = os.path.join(
        CARPETA_ARCHIVOS, carpeta_paciente)

    if not os.path.exists(ruta_carpeta_paciente):
        os.makedirs(ruta_carpeta_paciente)

    # Función auxiliar para copiar archivos
    def copiar_archivos_aux(archivos):
        if archivos:
            archivos_lista = archivos.split(';')
            nuevos_archivos = []

            for archivo in archivos_lista:
                if archivo:
                    nombre_archivo = os.path.basename(archivo)
                    ruta_destino = os.path.join(
                        ruta_carpeta_paciente, nombre_archivo)

                    # Verifica si el archivo ya existe en la carpeta de destino
                    if os.path.exists(ruta_destino):
                        # Si el archivo ya existe, no lo copies
                        continue
                    else:
                        # Si el archivo no existe, cópialo
                        try:
                            shutil.copy(archivo, ruta_destino)
                            nuevos_archivos.append(ruta_destino)
                        except FileNotFoundError:
                            print(f"Archivo no encontrado: {archivo}")

            return ';'.join(nuevos_archivos)
        return ''

    # Copiar archivos a la carpeta del paciente
    fotos = copiar_archivos_aux(fotos)
    videos = copiar_archivos_aux(videos)
    pdfs = copiar_archivos_aux(pdfs)
