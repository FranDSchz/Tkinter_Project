# datos.py
"""
Módulo de Datos

Centraliza la información estática de la aplicación.
Inicialmente, contiene una lista mínima de países para establecer la estructura.
Otras tareas se encargarán de poblar más este diccionario.
"""

DATOS_PAISES = {
    "Argentina": {
        "timezone": "America/Argentina/Buenos_Aires",
        "idioma": "Español",
        "dato_turistico": "Hogar del tango y de la vasta Patagonia.",
        "hemisferio": "Sur",
        "moneda_codigo": "ARS",
        "moneda_nombre": "Peso Argentino"
    },
    "Japón": {
        "timezone": "Asia/Tokyo",
        "idioma": "Japonés",
        "dato_turistico": "Conocido por sus templos, el Monte Fuji y la flor de cerezo.",
        "hemisferio": "Norte",
        "moneda_codigo": "JPY",
        "moneda_nombre": "Yen Japonés"
    }
}