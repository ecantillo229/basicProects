import tkinter as tk
root = tk.Tk()
root.title("Lista de tareas")
root.geometry("296x265")

listaTareas = []

def añadirTarea ():
    tarea = entrada.get()
    listaTareas.append(tarea)
    entrada.delete(0, tk.END)
    desplegable.insert(tk.END, tarea)

def eliminarTarea():
    tareaSeleccionada = desplegable.get(desplegable.curselection())
    listaTareas.remove(tareaSeleccionada)
    desplegable.delete(desplegable.curselection())

def guardarTarea():
    with open("tareas_pendientes.txt", "w") as archivo:
        for tarea in listaTareas:
            archivo.write(tarea + "\n")

def cargarTarea():
    with open("tareas_pendientes.txt", "r") as archivo:
        tareas = archivo.readlines()
    for tarea in tareas:
        tarea = tarea.strip()
        listaTareas.append(tarea)
        desplegable.insert(tk.END, tarea)

titulo = tk.Label(root,
text= "Lista de tareas")
titulo.place(relwidth= 1, relheight= 0.15)

entrada = tk.Entry(root)
entrada.place(relx= 0, rely= .15, relwidth= .7, relheight= .15)

botonAñadir = tk.Button(root,
text= "Añadir",
command= añadirTarea)
botonAñadir.place(relx= .7, rely= .15, relwidth= .3, relheight= .15)

desplegable = tk.Listbox(root)
desplegable.place(relx= 0, rely= .3, relwidth= 1, relheight= .55)

botonEliminar = tk.Button(root,
text= "Eliminar",
command= eliminarTarea)
botonEliminar.place(relx= 0, rely= .85, relwidth= .33, relheight= .15)

botonGuardar = tk.Button(root,
text= "Guardar",
command= guardarTarea)
botonGuardar.place(relx= .33, rely= .85, relwidth= .33, relheight= .15)

botonCargar = tk.Button(root,
text= "Cargar",
command= cargarTarea)
botonCargar.place(relx= .66, rely= .85, relwidth= .33, relheight= .15)


root.mainloop()