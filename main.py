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
from tkinter import ttk
# Este bloque se asegura de que el código solo se ejecute cuando se corre este archivo directamente.
if __name__ == "__main__":
    # 1. Crear la ventana raíz
    root = tk.Tk()
    
    # 2. Seleccionar los estilos
    style = ttk.Style()
    style.theme_use('clam')

    BG_COLOR = "#1e1e1e"
    FG_COLOR = "#dcdcdc"
    
    style.configure("Main.TFrame", background=BG_COLOR)
    style.configure("White.TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Helvetica", 11))
    style.configure("Clock.TLabel", background=BG_COLOR, foreground="cyan", font=("Consolas", 48, "bold"))
    style.configure("White.TLabelframe", background=BG_COLOR, relief="solid", borderwidth=1)
    # Estilo para el texto "Información" del LabelFrame
    style.configure("White.TLabelframe.Label", background=BG_COLOR, foreground=FG_COLOR, font=("Helvetica", 11, "bold"))
    style.configure("Info.TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Helvetica", 10))
    # 3. Crear una instancia de nuestra aplicación, pasándole la ventana raíz
    app = WorldTimeApp(root)
    
    # 4. Lanzar el bucle principal que mantiene la ventana abierta y receptiva
    root.mainloop()