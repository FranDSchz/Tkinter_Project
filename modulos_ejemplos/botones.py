import tkinter as tk

ventana = tk.Tk()
ventana.title('¡Ahora tenemos 3 botones!')
ventana.geometry('400x200')

boton1 = tk.Button(ventana, text="Botón 1")
boton2 = tk.Button(ventana, text="Botón 2")
boton3 = tk.Button(ventana, text="Botón 3")

boton1.pack(side="top")
boton2.pack(side="left")
boton3.pack(side="right")

ventana.mainloop()