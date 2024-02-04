import tkinter as tk
from tkinter import messagebox
import pickle

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tareas = []

        self.lista_box = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.lista_box.pack(pady=10)

        self.entry_tarea = tk.Entry(root, width=30)
        self.entry_tarea.pack(pady=5)

        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_como_completada)
        self.boton_completar.pack(pady=5)

        self.boton_guardar = tk.Button(root, text="Guardar Lista", command=self.guardar_lista)
        self.boton_guardar.pack(pady=5)

        self.boton_cargar = tk.Button(root, text="Cargar Lista", command=self.cargar_lista)
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
