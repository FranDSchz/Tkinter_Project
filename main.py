# main.py
"""
Punto de Entrada Principal de la Aplicación

Este script inicia la aplicación. Su responsabilidad es:
1. Crear la ventana principal de Tkinter.
2. Instanciar la clase principal de la UI (`WorldTimeApp`).
3. Iniciar el bucle de eventos de la aplicación.
"""
import tkinter as tk
from ui import WorldTimeApp

# Este bloque se asegura de que el código solo se ejecute cuando se corre este archivo directamente.
if __name__ == "__main__":
    # 1. Crear la ventana raíz
    root = tk.Tk()
    
    # 2. Crear una instancia de nuestra aplicación, pasándole la ventana raíz
    app = WorldTimeApp(root)
    
    # 3. Lanzar el bucle principal que mantiene la ventana abierta y receptiva
    root.mainloop()