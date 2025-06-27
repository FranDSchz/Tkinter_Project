# ui.py
"""
Módulo de Interfaz de Usuario (UI)

Contiene la clase principal `WorldTimeApp` que construye y controla la ventana.
Esta es la versión inicial y mínima para asegurar que la app se puede ejecutar.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# Importamos nuestros datos. Si esto funciona, la modularización es correcta.
from datos import DATOS_PAISES

class WorldTimeApp:
    def __init__(self, root):
        """Constructor de la clase. Configura la ventana inicial."""
        self.root = root
        self.root.title("Reloj Mundial por País")
        self.root.geometry("500x300")
        self.root.config(bg="black")

        # Etiqueta de título
        tk.Label(
            self.root,
            text="🌍 Seleccioná un país para ver su hora actual",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="black"
        ).pack(pady=15)

        # Combobox con los países cargados desde datos.py
        self.combo_paises = ttk.Combobox(self.root, values=list(DATOS_PAISES.keys()), state="readonly", width=40)
        self.combo_paises.pack(pady=10)
        
        # Etiqueta donde se mostrará la hora actual del país seleccionado
        self.label_hora = tk.Label(self.root, text="", font=("Consolas", 16), fg="cyan", bg="black")
        self.label_hora.pack(pady=10)

        # Etiqueta donde se muestra información adicional del país
        self.label_info = tk.Label(self.root, text="", font=("Helvetica", 12), fg="white", bg="black", wraplength=480, justify="left")
        self.label_info.pack(pady=10)

        # Variable para controlar actualización en loop
        self.timer_id = None

        # Conectamos el evento del combobox con la función que muestra la hora
        self.combo_paises.bind("<<ComboboxSelected>>", self.al_seleccionar)

    def mostrar_hora(self):
        pais = self.combo_paises.get()
        if not pais:
            return
        zona = DATOS_PAISES[pais]["timezone"]
        ahora = datetime.now(pytz.timezone(zona)).strftime("%H:%M:%S")
        self.label_hora.config(text=f"Hora actual en {pais}: {ahora}")
        
        datos = DATOS_PAISES[pais]
        texto = (
            f"Idioma: {datos['idioma']}\n"
            f"Moneda: {datos['moneda_nombre']} ({datos['moneda_codigo']})\n"
            f"Hemisferio: {datos['hemisferio']}\n"
            f"Dato turístico: {datos['dato_turistico']}"
        )
        self.label_info.config(text=texto)

        # Actualización en loop cada segundo
        self.timer_id = self.root.after(1000, self.mostrar_hora)

    def al_seleccionar(self, event):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.mostrar_hora()
