import tkinter as tk
from tkinter import messagebox  # Para mostrar mensajes de información, advertencia o error


# Clase que representa una tarea individual
class Task:
    def __init__(self, title, description, task_type):
        # Inicializa la tarea con un título, descripción y tipo
        self.title = title
        self.description = description
        self.task_type = task_type
        self.completed = False  # Estado inicial: no completada

    def mark_completed(self):
        # Cambia el estado de la tarea a completada
        self.completed = True

    def __str__(self):
        # Devuelve una representación en texto de la tarea
        status = "Completada" if self.completed else "Pendiente"
        return f"[{status}] {self.title} - {self.task_type}"


# Clase principal de la aplicación To-Do List
class ToDoListApp:
    def __init__(self, root):
        self.root = root  # Ventana principal
        self.root.title("To-Do List App")  # Título de la ventana principal
        self.root.geometry("600x400")  # Tamaño fijo de la ventana
        self.root.resizable(False, False)  # Deshabilitar redimensionamiento

        self.tasks = []  # Lista que almacenará las tareas

        # Marco principal para organizar los widgets
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=10)

        # Etiqueta de título
        tk.Label(self.main_frame, text="To-Do List", font=("Helvetica", 16)).pack()

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.main_frame, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Marco para los botones principales
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack()

        # Botones principales
        tk.Button(button_frame, text="Agregar Tarea", command=self.add_task_window).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Ver Detalles", command=self.view_task_details).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Completar Tarea", command=self.mark_task_completed).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task).grid(row=0, column=3, padx=5)

    def refresh_task_list(self):
        # Actualiza la lista de tareas en el Listbox
        self.task_listbox.delete(0, tk.END)  # Limpia la lista actual
        for i, task in enumerate(self.tasks):
            status = "✔" if task.completed else "✗"  # Icono según el estado de la tarea
            self.task_listbox.insert(tk.END, f"{i + 1}. {status} {task.title}")

    def add_task_window(self):
        # Abre una ventana secundaria para agregar una nueva tarea
        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Nueva Tarea")  # Título de la ventana
        add_window.geometry("400x250")  # Tamaño fijo de la ventana secundaria
        add_window.resizable(False, False)

        # Campos para ingresar los datos de la nueva tarea
        tk.Label(add_window, text="Título").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(add_window)  # Entrada para el título
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Descripción").grid(row=1, column=0, padx=5, pady=5)
        description_entry = tk.Entry(add_window)  # Entrada para la descripción
        description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Tipo").grid(row=2, column=0, padx=5, pady=5)
        task_type_var = tk.StringVar(add_window)  # Variable para almacenar el tipo seleccionado
        task_type_var.set("trabajo")  # Valor predeterminado

        # Menú desplegable para seleccionar el tipo de tarea
        task_type_menu = tk.OptionMenu(add_window, task_type_var, "trabajo", "casa", "negocios")
        task_type_menu.grid(row=2, column=1, padx=5, pady=5)

        def add_task_action():
            # Lógica para agregar la tarea
            title = title_entry.get()
            description = description_entry.get()
            task_type = task_type_var.get()
            if title and description and task_type:
                new_task = Task(title, description, task_type)  # Crea una nueva tarea
                self.tasks.append(new_task)  # Agrega la tarea a la lista
                self.refresh_task_list()  # Actualiza la lista de tareas
                messagebox.showinfo("Éxito", "Tarea agregada con éxito")  # Mensaje de éxito
                add_window.destroy()  # Cierra la ventana secundaria
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")  # Mensaje de error

        # Botón para confirmar la adición de la tarea
        tk.Button(add_window, text="Agregar", command=add_task_action).grid(row=3, column=0, columnspan=2, pady=10)

    def view_task_details(self):
        # Muestra los detalles de la tarea seleccionada
        selected_index = self.task_listbox.curselection()  # Índice de la tarea seleccionada
        if selected_index:
            task = self.tasks[selected_index[0]]
            # Detalles de la tarea en formato de texto
            details = f"Título: {task.title}\nDescripción: {task.description}\nTipo: {task.task_type}\nEstado: {'Completada' if task.completed else 'Pendiente'}"
            messagebox.showinfo("Detalles de la Tarea", details)  # Muestra los detalles en un cuadro de diálogo
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para ver detalles")  # Advertencia si no se selecciona ninguna tarea

    def mark_task_completed(self):
        # Marca una tarea como completada
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.mark_completed()  # Cambia el estado de la tarea
            self.refresh_task_list()  # Actualiza la lista de tareas
            messagebox.showinfo("Éxito", "Tarea marcada como completada")  # Mensaje de éxito
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")  # Advertencia si no se selecciona ninguna tarea

    def delete_task(self):
        # Elimina una tarea de la lista
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])  # Elimina la tarea de la lista
            self.refresh_task_list()  # Actualiza la lista de tareas
            messagebox.showinfo("Éxito", f"Tarea '{task.title}' eliminada")  # Mensaje de éxito
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")  # Advertencia si no se selecciona ninguna tarea


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = ToDoListApp(root)  # Inicializa la aplicación
    root.mainloop()  # Inicia el bucle principal de Tkinter
