import tkinter as tk
from tkinter import messagebox, ttk
from forms import ventana_agregar_paciente, ventana_buscar_paciente, ventana_eliminar_paciente, ventana_modificar_paciente, ventana_mostrar_info_paciente
from database import crear_base_datos, obtener_pacientes, buscar_paciente

# Ventana principal
app = tk.Tk()
app.title("Gestión de Pacientes")
app.geometry("400x600")

# Listbox para mostrar pacientes
listbox_pacientes = tk.Listbox(app, width=40, height=20)
listbox_pacientes.pack(padx=20, pady=20)

# Funcion para actualizar el listbox


def actualizar_listbox():
    listbox_pacientes.delete(0, tk.END)
    pacientes = obtener_pacientes()
    for paciente in pacientes:
        listbox_pacientes.insert(tk.END, f"{paciente[1]} {paciente[2]}")


# Crear base de datos al iniciar el programa
crear_base_datos()

# Actualizar el listbox al iniciar
actualizar_listbox()

# Funcion para mostrar la informacion del paciente al hacer doble click


def mostrar_info_paciente(event=None):
    seleccionado = listbox_pacientes.curselection()
    if seleccionado:
        nombre_completo = listbox_pacientes.get(seleccionado)
        nombres = nombre_completo.split()
        print(f"Nombre completo: {nombre_completo}, Nombres: {nombres}")

        # Intenta buscar con los primeros dos nombres y los últimos dos nombres
        if len(nombres) >= 4:
            paciente1 = buscar_paciente(nombres[0], nombres[1])
            paciente2 = buscar_paciente(nombres[0], nombres[-1])
            paciente3 = buscar_paciente(nombres[0], nombres[-2])
            paciente = paciente1 or paciente2 or paciente3
        else:
            paciente = buscar_paciente(nombres[0], nombres[1])

        if paciente:
            print("Paciente encontrado")
            ventana_mostrar_info_paciente(paciente)
        else:
            print("Paciente no encontrado")
    else:
        print("No se seleccionó un paciente")


# Configura el doble click en el listbox
listbox_pacientes.bind("<Double-Button-1>", mostrar_info_paciente)


# Menú Principal
menu_principal = tk.Menu(app)
app.config(menu=menu_principal)

# Opción de menú para mostrar opciones
menu_principal.add_command(label="Agregar Paciente",
                           command=lambda: ventana_agregar_paciente(actualizar_listbox))
menu_principal.add_command(label="Buscar Paciente",
                           command=ventana_buscar_paciente)
menu_principal.add_command(label="Eliminar Paciente",
                           command=lambda: ventana_eliminar_paciente(actualizar_listbox))
menu_principal.add_command(label="Modificar Paciente",
                           command=lambda: [ventana_modificar_paciente(), actualizar_listbox()])

app.mainloop()
