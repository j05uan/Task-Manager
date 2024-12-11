# db_operations.py
from models import Task, TaskStatus
from config import Session

# Función para agregar una tarea nueva (básica, pero efectiva)
def add_task(title, description):
    session = Session()
    
    # Vamos a verificar si la tarea ya existe (aunque no es la mejor forma, pero bueno)
    existing_task = session.query(Task).filter(Task.title == title).first()
    if existing_task:  # Si la tarea existe, no la agregamos
        print(f"Tarea con el título '{title}' ya existe.")  # Mensaje de que ya existe
        session.close()
        return  # No agregamos la tarea
    
    task = Task(title=title, description=description)  # Creamos la tarea
    session.add(task)  # Añadimos a la base de datos
    session.commit()  # Guardamos los cambios
    session.close()  # Cerramos la sesión
    print(f"Tarea '{title}' agregada.")  # Confirmación

# Función para listar las tareas
def list_tasks(status_filter="Todos"):  # Filtro por estado
    session = Session()
    
    # Aquí empezamos con el filtro (no tan limpio, pero efectivo)
    if status_filter == "Pendiente":
        tasks = session.query(Task).filter(Task.status == TaskStatus.PENDING).all()  # Filtrar solo pendientes
    elif status_filter == "Completada":
        tasks = session.query(Task).filter(Task.status == TaskStatus.COMPLETED).all()  # Filtrar completadas
    else:
        tasks = session.query(Task).all()  # Si no hay filtro, listamos todas

    # Imprimimos todas las tareas
    for task in tasks:
        print(f"{task.id}. {task.title} - {task.status.value}")  # Simple output de tarea
    session.close()  # Cerramos sesión

# Marcar una tarea como completada (sencillo pero útil)
def mark_task_completed(task_id):
    session = Session()
    
    # Buscamos la tarea con el ID
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:  # Si la tarea existe
        task.status = TaskStatus.COMPLETED  # Cambiamos el estado a completada
        session.commit()  # Guardamos los cambios
        print(f"Tarea {task_id} marcada como completada.")  # Confirmación
    session.close()  # Cerramos sesión

# Eliminar tareas completadas (nada sofisticado)
def delete_completed_tasks():
    session = Session()
    
    # Buscamos todas las tareas completadas
    completed_tasks = session.query(Task).filter(Task.status == TaskStatus.COMPLETED).all()
    
    # Borramos cada tarea completada
    for task in completed_tasks:
        session.delete(task)  # Eliminamos tarea
        print(f"Tarea {task.id} eliminada.")  # Confirmación

    session.commit()  # Confirmamos los cambios
    session.close()  # Cerramos sesión
