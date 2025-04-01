Gestión de Pacientes
Este proyecto es una aplicación de escritorio desarrollada en Python que permite gestionar información de pacientes, incluyendo datos personales, diagnósticos, evolución, tratamiento y archivos asociados (fotos, videos y PDFs). Los datos se almacenan en una base de datos SQLite y los archivos se organizan en carpetas específicas dentro del directorio del usuario.

Características
Gestión completa de pacientes:

Agregar nuevos pacientes.

Buscar pacientes por nombre y apellido.

Modificar información existente.

Eliminar pacientes del sistema.

Organización de archivos:

Posibilidad de asociar fotos, videos y documentos PDF a cada paciente.

Copia automática de archivos a carpetas específicas dentro del directorio del usuario.

Interfaz gráfica:

Interfaz intuitiva creada con tkinter, con formularios para cada funcionalidad.

Base de datos local:

Uso de SQLite para almacenar la información de los pacientes.

Requisitos del sistema
Python 3.8 o superior.

Bibliotecas necesarias:

tkinter (incluida por defecto en Python).

sqlite3 (incluida por defecto en Python).

shutil (incluida por defecto en Python).

Instalación
Clona este repositorio o descarga los archivos del proyecto.

Asegúrate de tener Python instalado en tu sistema.

Ejecuta el archivo principal:

bash
python main.py
Estructura del proyecto
Archivo	Descripción
main.py	Archivo principal que inicia la aplicación y gestiona el flujo general.
forms.py	Contiene las ventanas y formularios para las diferentes acciones (agregar, buscar, modificar, etc.).
database.py	Lógica para interactuar con la base de datos SQLite (crear, leer, actualizar y eliminar registros).
utils.py	Funciones auxiliares para gestionar archivos asociados a los pacientes.
Cómo usar
Ejecuta el programa con:

bash
python main.py
Selecciona la acción que deseas realizar desde el menú principal:

Agregar Paciente: Completa el formulario con los datos del paciente y selecciona los archivos asociados (opcional).

Buscar Paciente: Ingresa el nombre y apellido del paciente para ver su información completa.

Modificar Paciente: Busca un paciente y actualiza su información o gestiona sus archivos asociados.

Eliminar Paciente: Busca un paciente y elimínalo del sistema.

Los datos se guardarán automáticamente en la base de datos local y los archivos se copiarán a carpetas organizadas dentro del directorio "Mis Documentos".

Notas técnicas
1. Base de datos (database.py)
La base de datos SQLite se crea automáticamente en la carpeta "Documents/GestionPacientes". Contiene una tabla llamada pacientes con los siguientes campos:

id: Identificador único.

nombre: Nombre del paciente.

apellido: Apellido del paciente.

edad, telefono, email: Información personal.

diagnostico, evolucion, tratamiento: Información médica.

fotos, videos, pdfs: Rutas a los archivos asociados.

2. Gestión de archivos (utils.py)
Los archivos asociados a cada paciente (fotos, videos, PDFs) se copian automáticamente a una carpeta específica dentro de "Documents/GestionPacientes/archivos_pacientes". Esto asegura que todos los archivos estén organizados y accesibles.

Contribución
Si deseas mejorar este proyecto:

Haz un fork del repositorio.

Crea una nueva rama:

bash
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y envía un pull request.

Autor
Este programa fue desarrollado, por Edelan, como una solución para gestionar información médica y organizar archivos relacionados con pacientes.

¡Gracias por usar este programa! 😊