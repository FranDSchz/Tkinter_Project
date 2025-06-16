import tkinter as tk
import time

# Datos de países con diferencia horaria respecto a Argentina 
# En esta estructura de datos podemos agregar un dato curioso del país 
# y también el equivalente de 1 unidad de la divisa en pesos Argentinos. Ej: 1 USD = 1200 ARS
paises_info = {
    'Argentina': {
        'divisa': 'Peso Argentino (ARS)',
        'diferencia': 0,
    },
    'Francia': {
        'divisa': 'Euro (EUR)',
        'diferencia': +5,
    },
    'Alemania': {
        'divisa': 'Euro (EUR)',
        'diferencia': +5,
    },
    'USA': {
        'divisa': 'Dólar estadounidense (USD)',
        'diferencia': -1,
    },
    'Mexico': {
        'divisa': 'Peso Mexicano (MXN)',
        'diferencia': -3,
    },
    'Brasil': {
        'divisa': 'Real Brasileño (BRL)',
        'diferencia': +1,
    },
    'Australia': {
        'divisa': 'Dólar Australiano (AUD)',
        'diferencia': +13,
    },
}

# Función que actualiza la hora automáticamente 
def actualizar_hora():
    if destino in paises_info:
        diferencia = paises_info[destino]['diferencia']
        hora_local = time.localtime(time.time() + diferencia * 3600)
        hora_formateada = time.strftime('%H:%M:%S', hora_local)
        hora_label.config(text=hora_formateada)
    else:
        hora_label.config(text="País no válido")
    ventana.after(1000, actualizar_hora) 

# Configuración de la interfaz 
ventana = tk.Tk()
ventana.title("Reloj por país")
ventana.geometry("300x200")

# Etiqueta del reloj
hora_label = tk.Label(ventana, font=("Arial", 30), bg="black", fg="white")
hora_label.pack(pady=20) #pady es el valor en eje y en el que se ubica el label de la hora

# Mostrar la hora automáticamente para el país seleccionado
destino = "Australia"  # Cambiar por el string del país seleccionado, acá iría el país que sea seleccionado de algún menú o lista

# Etiqueta con nombre del país
pais_label = tk.Label(ventana, text=f"Hora en {destino}", font=("Arial", 12))
pais_label.pack(pady=5) #pady es el valor en eje y en el que se ubica el label del país

actualizar_hora()
ventana.mainloop()
