## Brenda Samara Escobar Avila
 
## 23005735

# To-Do List App

## Descripción
La **To-Do List App** es una aplicación sencilla para gestionar tareas pendientes. Permite agregar, listar, completar y eliminar tareas, así como visualizar los detalles de cada una. Esta herramienta es ideal para organizar actividades personales o profesionales.

---

## Características
1. **Pantalla Principal:**
   - Muestra una lista de tareas pendientes y completadas.
   - Incluye opciones para agregar, completar, eliminar y ver detalles de las tareas.

2. **Agregar Tarea:**
   - Permite especificar un título, una descripción y un tipo de tarea (trabajo, casa o negocios).
   - Valida que todos los campos sean obligatorios antes de agregar la tarea.

3. **Lista de Tareas:**
   - Muestra las tareas con un indicador visual: ✔ para tareas completadas y ✗ para tareas pendientes.
   - Permite seleccionar una tarea para realizar acciones.

4. **Detalles de Tarea:**
   - Muestra toda la información de la tarea seleccionada, incluyendo su título, descripción, tipo y estado.

5. **Generar PDF:**
   - Genera un documento PDF que incluye la URL del repositorio, un wireframe de la aplicación y las instrucciones para usarla.

---

## Requisitos
- **Python 3.7 o superior**
- Bibliotecas:
  - `tkinter` (incluido en Python por defecto)
  - `reportlab` (instalar con `pip install reportlab`)

---

## Instalación
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/SamyER33/23005735_PF_IDAM.git
   cd repo-todolist
2. **Instalar dependencias (si es necesario):**
    ```bash
    pip install reportlab
3. **Ejecutar la aplicación:**
    ```bash
    python main.py

## Uso

1. **Pantalla Principal:**
    - Visualiza todas las tareas.
    - Usa los botones para interactuar:
        - Agregar Tarea: Abre un formulario para ingresar detalles de una nueva tarea.
        - Ver Detalles: Muestra información detallada de la tarea seleccionada.
        - Completar Tarea: Marca una tarea como completada.
        - Eliminar Tarea: Elimina la tarea seleccionada de la lista.
2. **Agregar Tarea:**
    - Ingresa un título, descripción y selecciona un tipo (trabajo, casa o negocios) en el formulario.
    - Presiona "Agregar" para guardar la tarea.
3. **Visualizar detalles:**
    - Selecciona una tarea de la lista.
    - Presiona "Ver Detalles" para mostrar su información.
4. **Eliminar o completar tareas:**
    - Selecciona una tarea y usa el botón correspondiente.

## Estructura del Código

1. **Clase `Task`**
    - Representa una tarea individual.
    - Atributos:
        - `title`: Título de la tarea.
        - `description`: Descripción detallada.
        - `task_type`: Tipo de tarea (trabajo, casa o negocios).
        - `completed`: Estado de la tarea (pendiente/completada).
    - Métodos:
        - `mark_completed()`: Marca la tarea como completada.
        - `__str__()`: Devuelve una representación en texto de la tarea.
2. **Clase ToDoListApp**
    - Gestiona la interfaz gráfica y las operaciones principales.
    - Funciones principales:
        - Pantalla Principal: Muestra la lista de tareas.
        - Agregar Tarea: Abre una ventana para ingresar una nueva tarea.
        - Ver Detalles: Muestra un cuadro de diálogo con la información de una tarea seleccionada.
        - Completar Tarea: Cambia el estado de una tarea a completada.
        - Eliminar Tarea: Elimina una tarea seleccionada.

## Wireframe
**Pantallas principales:**
1. **Pantalla Principal:** Lista de tareas con botones para interactuar.
2. **Agregar Tarea:** Formulario para ingresar nueva tarea.
3. **Detalles de Tarea:** Ventana emergente con información de la tarea seleccionada.