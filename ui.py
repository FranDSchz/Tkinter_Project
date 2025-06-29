# ui.py
"""
Módulo de Interfaz de Usuario (UI) - Versión Sprint 2

Añade la funcionalidad del conversor de divisas.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pytz
from PIL import Image, ImageTk


# Importamos las tasas de cambio desde nuestro módulo de datos
from datos import DATOS_PAISES, TASA_ARS_A_USD, TASAS_A_USD

class WorldTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WorldTime+ con Conversor")
        # Aumentamos un poco la altura de la ventana para el conversor
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.root.config(bg="#1e1e1e")

        self.crear_widgets()
        self.actualizar_reloj()

    def crear_widgets(self):
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Creamos un Frame superior para alinear la bandera y el selector
        top_frame = ttk.Frame(main_frame, style="Main.TFrame")
        top_frame.pack(fill=tk.X)

        # Añadimos un Label vacío que contendrá la imagen de la bandera
        self.bandera_label = ttk.Label(top_frame, style="Main.TLabel")
        self.bandera_label.pack(side=tk.LEFT, padx=(0, 15))

        # Metemos el selector y su etiqueta dentro de su propio Frame para mejor control
        selector_frame = ttk.Frame(top_frame, style="Main.TFrame")
        selector_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Esto que ya tenías, ahora va dentro de 'selector_frame'
        ttk.Label(selector_frame, text="Selecciona un País:", style="White.TLabel").pack(fill=tk.X)
        self.pais_seleccionado = tk.StringVar()
        combo_paises = ttk.Combobox(selector_frame, textvariable=self.pais_seleccionado,
                                    values=list(DATOS_PAISES.keys()), state='readonly', width=30)
        combo_paises.pack(pady=(5, 0), fill=tk.X)
        combo_paises.current(0)
        combo_paises.bind("<<ComboboxSelected>>", self.actualizar_info)

        # --- SECCIÓN DE RELOJ  ---
        self.hora_label = ttk.Label(main_frame, text="--:--:--", style="Clock.TLabel")
        self.hora_label.pack(pady=10) 

        # --- SECCIÓN DE INFORMACIÓN ADICIONAL ---
        info_frame = ttk.LabelFrame(main_frame, text="Información", style="White.TLabelframe")
        info_frame.pack(pady=20, fill=tk.X)
        self.idioma_label = ttk.Label(info_frame, text="Idioma: -", style="Info.TLabel")
        self.idioma_label.pack(anchor="w", padx=10, pady=5)
        self.estacion_label = ttk.Label(info_frame, text="Estación: -", style="Info.TLabel")
        self.estacion_label.pack(anchor="w", padx=10, pady=5)
        self.dato_label = ttk.Label(info_frame, text="Dato: -", style="Info.TLabel", wraplength=500, justify="left")
        self.dato_label.pack(anchor="w", padx=10, pady=5)

        # --- CAMBIO 1: AÑADIR ESTE WIDGET ---
        self.diferencia_horaria_label = ttk.Label(info_frame, text="Diferencia: -", style="Info.TLabel")
        self.diferencia_horaria_label.pack(anchor="w", padx=10, pady=5)
        # SECCIÓN DEL CONVERSOR DE DIVISAS ---
        conversor_frame = ttk.LabelFrame(main_frame, text="Conversor de Divisas (ARS a destino)", style="White.TLabelframe")
        conversor_frame.pack(pady=10, fill=tk.X)

        # Frame para la entrada de datos (Monto y botón)
        input_frame = ttk.Frame(conversor_frame, style="Main.TFrame")
        input_frame.pack(padx=10, pady=10, fill=tk.X)
        
        ttk.Label(input_frame, text="Monto en ARS:", style="White.TLabel").pack(side=tk.LEFT, padx=(0, 10))
        
        self.monto_entry = ttk.Entry(input_frame, font=("Helvetica", 10))
        self.monto_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        convertir_btn = ttk.Button(input_frame, text="Convertir", command=self.convertir_divisa)
        convertir_btn.pack(side=tk.LEFT, padx=(10, 0))

        # Label para mostrar el resultado de la conversión
        self.resultado_conversion_label = ttk.Label(conversor_frame, text="Resultado...", style="Info.TLabel")
        self.resultado_conversion_label.pack(padx=10, pady=(0, 10))
        
        self.actualizar_info()

    def actualizar_info(self, event=None):
        nombre_pais = self.pais_seleccionado.get()
        if not nombre_pais: return
        datos = DATOS_PAISES[nombre_pais]
        try:
            # Construimos la ruta al archivo de la bandera
            ruta_bandera = f"flags/{datos['bandera_img']}"
            
            # Abrimos la imagen, la redimensionamos y la preparamos para Tkinter
            imagen = Image.open(ruta_bandera)
            imagen_redimensionada = imagen.resize((64, 42), Image.Resampling.LANCZOS)
            foto_bandera = ImageTk.PhotoImage(imagen_redimensionada)
            
            # Asignamos la imagen al Label que creamos antes
            self.bandera_label.config(image=foto_bandera)
            
            # Guardamos una referencia para que Python no la borre (muy importante)
            self.bandera_label.image = foto_bandera

        except (FileNotFoundError, KeyError):
            # Si el archivo no existe o la clave "bandera_img" no está en datos.py
            self.bandera_label.config(image='') # Limpiamos la imagen
            # Opcional: imprimir un aviso en la consola para depuración
            # print(f"Advertencia: No se encontró la bandera para {nombre_pais}")
        except Exception as e:
            # Para cualquier otro error al cargar la imagen
            self.bandera_label.config(image='')
            # print(f"Error al cargar la bandera: {e}")
        
        self.idioma_label.config(text=f"Idioma: {datos['idioma']}")
        self.dato_label.config(text=f"Dato: {datos['dato_turistico']}")
        estacion = self.obtener_estacion(datos['hemisferio'])
        self.estacion_label.config(text=f"Estación actual: {estacion}")
        try:
            # Definimos las zonas horarias
            tz_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
            tz_destino = pytz.timezone(datos["timezone"])

            # Obtenemos el offset (diferencia con UTC) para cada zona
            offset_argentina = datetime.now(tz_argentina).utcoffset()
            offset_destino = datetime.now(tz_destino).utcoffset()

            # Calculamos la diferencia y la pasamos a horas
            diferencia_en_horas = (offset_destino - offset_argentina).total_seconds() / 3600

            # Formateamos el texto para mostrar
            if diferencia_en_horas == 0:
                texto_diferencia = "Misma zona horaria que Argentina"
            elif diferencia_en_horas > 0:
                texto_diferencia = f"+{int(diferencia_en_horas)} horas respecto a Argentina"
            else:
                texto_diferencia = f"{int(diferencia_en_horas)} horas respecto a Argentina"
            
            self.diferencia_horaria_label.config(text=texto_diferencia)

        except Exception as e:
            self.diferencia_horaria_label.config(text="Diferencia: No disponible")
            print(f"Error calculando diferencia horaria: {e}")

        # Limpiar el resultado del conversor cada vez que se cambia de país
        self.resultado_conversion_label.config(text="Resultado...")
        self.monto_entry.delete(0, tk.END)

        self.actualizar_reloj()

    def actualizar_reloj(self):
        # (Sin cambios en esta función)
        try:
            nombre_pais = self.pais_seleccionado.get()
            if nombre_pais:
                tz_string = DATOS_PAISES[nombre_pais]["timezone"]
                tz = pytz.timezone(tz_string)
                hora_actual = datetime.now(tz).strftime('%H:%M:%S')
                self.hora_label.config(text=hora_actual)
        except Exception:
            self.hora_label.config(text="--:--:--")
        self.root.after(1000, self.actualizar_reloj)

    def obtener_estacion(self, hemisferio):
        # (Sin cambios en esta función)
        mes = datetime.now().month
        if hemisferio == 'Norte':
            if mes in (3, 4, 5): return "Primavera"
            if mes in (6, 7, 8): return "Verano"
            if mes in (9, 10, 11): return "Otoño"
            return "Invierno"
        elif hemisferio == 'Sur':
            if mes in (3, 4, 5): return "Otoño"
            if mes in (6, 7, 8): return "Invierno"
            if mes in (9, 10, 11): return "Primavera"
            return "Verano"
        return "Desconocida"

    # --- NUEVO: FUNCIÓN DE LÓGICA PARA LA CONVERSIÓN ---
    def convertir_divisa(self):
        """
        Toma el monto ingresado, lo convierte a la moneda del país seleccionado
        y muestra el resultado en la etiqueta.
        """
        # 1. Obtener y validar el monto ingresado
        try:
            monto_ars = float(self.monto_entry.get())
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingresa un monto numérico válido.")
            return

        # 2. Obtener la moneda del país de destino
        nombre_pais = self.pais_seleccionado.get()
        moneda_destino_codigo = DATOS_PAISES[nombre_pais]["moneda_codigo"]

        # 3. Realizar el cálculo
        # Primero, pasamos el monto en ARS a nuestra moneda de referencia, USD.
        monto_en_usd = monto_ars * TASA_ARS_A_USD
        
        # Luego, convertimos de USD a la moneda de destino.
        tasa_destino = TASAS_A_USD[moneda_destino_codigo]
        resultado_final = monto_en_usd * tasa_destino

        # 4. Formatear y mostrar el resultado
        resultado_texto = f"{monto_ars:,.2f} ARS son aprox. {resultado_final:,.2f} {moneda_destino_codigo}"
        self.resultado_conversion_label.config(text=resultado_texto)