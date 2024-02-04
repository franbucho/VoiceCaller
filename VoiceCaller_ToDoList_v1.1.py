import tkinter as tk
from tkinter import ttk, messagebox
import pickle

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tareas = []

        # Crear un estilo para los widgets tematizados (ttk)
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, relief="flat", background="#262525", foreground="gray", font=("Helvetica", 12))
        self.style.configure("TEntry", padding=5, relief="flat", background="#e3dcdc", font=("Helvetica", 12))

        # Lista
        self.lista_box = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bd=0, font=("Helvetica", 12))
        self.lista_box.pack(pady=10)

        # Entrada de tarea
        self.entry_tarea = ttk.Entry(root, width=30)
        self.entry_tarea.pack(pady=5)

        # Botones
        self.boton_agregar = ttk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = ttk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        self.boton_completar = ttk.Button(root, text="Marcar como Completada", command=self.marcar_como_completada)
        self.boton_completar.pack(pady=5)

        self.boton_guardar = ttk.Button(root, text="Guardar Lista", command=self.guardar_lista)
        self.boton_guardar.pack(pady=5)

        self.boton_cargar = ttk.Button(root, text="Cargar Lista", command=self.cargar_lista)
        self.boton_cargar.pack(pady=5)

        self.cargar_lista()

    def agregar_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def marcar_como_completada(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice] = f"{self.tareas[indice]} (Completada)"
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_box.insert(tk.END, tarea)

    def guardar_lista(self):
        with open("lista_tareas.pkl", "wb") as archivo:
            pickle.dump(self.tareas, archivo)
        messagebox.showinfo("Guardado", "Lista de tareas guardada correctamente.")

    def cargar_lista(self):
        try:
            with open("lista_tareas.pkl", "rb") as archivo:
                self.tareas = pickle.load(archivo)
            self.actualizar_lista()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
