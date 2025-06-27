# ui.py
"""
Módulo de Interfaz de Usuario (UI)

Contiene la clase principal `WorldTimeApp` que construye y controla la ventana.
Esta es la versión inicial y mínima para asegurar que la app se puede ejecutar.
"""

import tkinter as tk
from tkinter import ttk

# Importamos nuestros datos. Si esto funciona, la modularización es correcta.
from datos import DATOS_PAISES

class WorldTimeApp:
    def __init__(self, root):
        """Constructor de la clase. Configura la ventana inicial."""
        self.root = root
        self.root.title("WorldTime+ (Base)")
        self.root.geometry("400x200")
        self.root.config(bg="#1e1e1e")

        self.crear_widgets()

    def crear_widgets(self):
        """Crea los widgets iniciales. Por ahora, solo un saludo."""
        # (Jueves, 26 de Junio de 2025)
        style = ttk.Style()
        style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Helvetica", 14))

        # Obtenemos la cantidad de países cargados desde nuestro módulo de datos
        num_paises = len(DATOS_PAISES)

        label_bienvenida = ttk.Label(
            self.root, 
            text=f"¡Base del Proyecto WorldTime+ lista!\n{num_paises} países cargados desde datos.py."
        )
        label_bienvenida.pack(pady=50, padx=20)