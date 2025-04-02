Patient Management
This project is a desktop application developed in Python that allows users to manage patient information, including personal details, diagnoses, progress, treatments, and associated files (photos, videos, and PDFs). Data is stored in a SQLite database, and files are organized into specific folders within the user's directory.

Features
Comprehensive Patient Management:
Add new patients.

Search for patients by name and surname.

Update existing information.

Delete patients from the system.

File Organization:
Associate photos, videos, and PDF documents with each patient.

Automatically copy files to specific folders within the user's directory.

Graphical Interface:
Intuitive interface built with tkinter, featuring forms for each functionality.

Local Database:
Uses SQLite to store patient information securely.

System Requirements
Python 3.8 or higher.

Required libraries:

tkinter (default in Python).

sqlite3 (default in Python).

shutil (default in Python).

Installation
Clone this repository or download the project files.

Ensure Python is installed on your system.

Run the main file:

bash
python main.py
Project Structure
File	Description
main.py	Main file that starts the application and manages the overall workflow.
forms.py	Contains windows and forms for actions like adding, searching, and editing.
database.py	Logic for interacting with the SQLite database (create, read, update, delete).
utils.py	Auxiliary functions for managing files associated with patients.
How to Use
Run the program:

bash
python main.py
Choose an action from the main menu:

Add Patient: Fill out the form with patient details and optionally select associated files.

Search Patient: Enter the patient's name and surname to view their complete information.

Edit Patient: Search for a patient and update their details or manage their associated files.

Delete Patient: Search for a patient and remove them from the system.

Data will be automatically saved in the local database, and associated files will be copied to organized folders within the "Documents" directory.

Technical Notes
1. Database (database.py)
The SQLite database is created automatically in the "Documents/GestionPacientes" folder. It includes a table called patients with fields such as:

id: Unique identifier.

name: Patient's first name.

surname: Patient's last name.

age, phone, email: Personal information.

diagnosis, progress, treatment: Medical information.

photos, videos, pdfs: Paths to associated files.

2. File Management (utils.py)
Associated files (photos, videos, PDFs) are automatically copied to a specific folder under "Documents/GestionPacientes/archivos_pacientes". This ensures all files are well-organized and easily accessible.

Contribution
If you want to improve this project:

Fork this repository.

Create a new branch:

bash
git checkout -b feature/new-feature
Make your changes and submit a pull request.

Author
This program was developed by Edelan as a solution for managing medical information and organizing patient-related files.

Thank you for using this application! 😊
