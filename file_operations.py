# Aquí trabajamos con el archivo JSON para guardar y cargar tareas

import json
from db_operations import Session, Task, TaskStatus

# Guardar tareas a un archivo JSON
def save_tasks_to_json(filename):
    try:
        session = Session()
        tasks = session.query(Task).all()  # Recuperamos todas las tareas
        tasks_data = [{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status.value} for task in tasks]
        
        with open(filename, 'w') as f:  # Abrimos el archivo para escribir
            json.dump(tasks_data, f, indent=4)  # Escribimos las tareas al archivo
        session.close()  # Cerramos sesión
        print(f"Tareas guardadas en {filename}.")  # Confirmación
    except Exception as e:
        print(f"Error al guardar tareas: {e}")  # Si hay un error, lo mostramos

# Cargar tareas desde un archivo JSON
def load_tasks_from_json(filename):
    try:
        with open(filename, 'r') as f:  # Abrimos el archivo para leer
            tasks_data = json.load(f)  # Cargamos las tareas desde el archivo
        
        session = Session()
        for task_data in tasks_data:  # Vamos a agregar las tareas al DB
            task = Task(title=task_data['title'], description=task_data['description'], status=TaskStatus[task_data['status']])
            session.add(task)  # Añadimos la tarea a la sesión
        session.commit()  # Guardamos los cambios
        session.close()  # Cerramos sesión
        print(f"Tareas cargadas desde {filename}.")  # Confirmación
    except Exception as e:
        print(f"Error al cargar tareas: {e}")  # Si hay un error, lo mostramos
