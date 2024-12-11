import streamlit as st
from db_operations import add_task, list_tasks, mark_task_completed, delete_completed_tasks
from file_operations import save_tasks_to_json, load_tasks_from_json

# ¡Empezamos! Esto es la interfaz de Streamlit
def app():
    st.title('Gestión de Tareas')

    # Formulario para agregar tarea, con la magia de Streamlit
    # Como puede ser un formulario largo, está algo desordenado
    with st.form(key="add_task_form"):
        title = st.text_input("Título de la tarea")  # Título de la tarea
        description = st.text_area("Descripción de la tarea")  # Descripción de la tarea
        submit_button = st.form_submit_button(label='Guardar tarea')  # Botón para agregar tarea

        # Si el usuario presiona el botón de guardar, guardamos la tarea
        if submit_button:
            if title and description:
                add_task(title, description)  # Función de la base de datos
                st.success(f"Tarea '{title}' agregada correctamente.")  # Mensaje de éxito
            else:
                st.error("Por favor, ingresa un título y una descripción.")  # Error si no se llena el formulario

    # Un filtro para ver las tareas pendientes o completadas
    st.header("Filtrar tareas")
    status_filter = st.radio("Filtrar por estado", ["Todos", "Pendiente", "Completada"])  # Opciones de filtro

    # Listamos las tareas (filtradas si es necesario)
    st.subheader("Lista de tareas:")
    list_tasks(status_filter)  # Función que muestra todas las tareas según el filtro

    # Ojo, aquí podemos marcar una tarea como completada (bastante simple)
    task_id = st.number_input("ID de la tarea a marcar como completada", min_value=1)  # ID de tarea
    if st.button('Marcar como completada'):  # Si el usuario presiona este botón...
        mark_task_completed(task_id)  # Marcar como completada

    # Si la gente quiere eliminar tareas completadas, pueden presionar este botón
    if st.button('Eliminar tareas completadas'):  # Eliminar tareas completadas
        delete_completed_tasks()  # Llamada a la función que elimina

    # Aquí podemos guardar las tareas en un archivo JSON
    if st.button('Guardar tareas a JSON'):  # Botón para guardar las tareas
        save_tasks_to_json('tasks.json')  # Guarda el archivo JSON con las tareas

    # Cargar tareas desde un archivo JSON
    if st.button('Cargar tareas desde JSON'):  # Botón para cargar las tareas
        load_tasks_from_json('tasks.json')  # Cargar desde el archivo

# Ejecutamos la app si es el archivo principal
if __name__ == '__main__':
    app()
