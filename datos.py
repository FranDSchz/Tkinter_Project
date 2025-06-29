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
    },
    "Estados Unidos": {
        "timezone": "America/New_York",
        "idioma": "Inglés",
        "dato_turistico": "Famoso por la Estatua de la Libertad y el Gran Cañón.",
        "hemisferio": "Norte",
        "moneda_codigo": "USD",
        "moneda_nombre": "Dólar estadounidense"
    },
    "Canadá": {
        "timezone": "America/Toronto",
        "idioma": "Inglés y Francés",
        "dato_turistico": "Conocido por sus paisajes naturales como las Cataratas del Niágara.",
        "hemisferio": "Norte",
        "moneda_codigo": "CAD",
        "moneda_nombre": "Dólar canadiense"
    },
    "México": {
        "timezone": "America/Mexico_City",
        "idioma": "Español",
        "dato_turistico": "Hogar de las antiguas ruinas mayas y aztecas.",
        "hemisferio": "Norte",
        "moneda_codigo": "MXN",
        "moneda_nombre": "Peso mexicano"
    },
    "Brasil": {
        "timezone": "America/Sao_Paulo",
        "idioma": "Portugués",
        "dato_turistico": "Famoso por el Cristo Redentor y el Carnaval de Río.",
        "hemisferio": "Sur",
        "moneda_codigo": "BRL",
        "moneda_nombre": "Real brasileño"
    },
    "Colombia": {
        "timezone": "America/Bogota",
        "idioma": "Español",
        "dato_turistico": "Reconocida por el café y Cartagena de Indias.",
        "hemisferio": "Norte",
        "moneda_codigo": "COP",
        "moneda_nombre": "Peso colombiano"
    },
    "Chile": {
        "timezone": "America/Santiago",
        "idioma": "Español",
        "dato_turistico": "Conocido por el desierto de Atacama y la Patagonia.",
        "hemisferio": "Sur",
        "moneda_codigo": "CLP",
        "moneda_nombre": "Peso chileno"
    },
    "Perú": {
        "timezone": "America/Lima",
        "idioma": "Español",
        "dato_turistico": "Famoso por Machu Picchu y la cultura incaica.",
        "hemisferio": "Sur",
        "moneda_codigo": "PEN",
        "moneda_nombre": "Sol peruano"
    },
    "España": {
        "timezone": "Europe/Madrid",
        "idioma": "Español",
        "dato_turistico": "Conocida por su arquitectura, gastronomía y flamenco.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Francia": {
        "timezone": "Europe/Paris",
        "idioma": "Francés",
        "dato_turistico": "Famosa por la Torre Eiffel y los vinos.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Italia": {
        "timezone": "Europe/Rome",
        "idioma": "Italiano",
        "dato_turistico": "Cuna del Imperio Romano y la pizza.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Alemania": {
        "timezone": "Europe/Berlin",
        "idioma": "Alemán",
        "dato_turistico": "Reconocido por el Muro de Berlín y sus castillos.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Reino Unido": {
        "timezone": "Europe/London",
        "idioma": "Inglés",
        "dato_turistico": "Famoso por el Big Ben y Buckingham Palace.",
        "hemisferio": "Norte",
        "moneda_codigo": "GBP",
        "moneda_nombre": "Libra esterlina"
    },
    "Portugal": {
        "timezone": "Europe/Lisbon",
        "idioma": "Portugués",
        "dato_turistico": "Destacado por sus playas y el fado.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Países Bajos": {
        "timezone": "Europe/Amsterdam",
        "idioma": "Neerlandés",
        "dato_turistico": "Conocido por sus canales, molinos y tulipanes.",
        "hemisferio": "Norte",
        "moneda_codigo": "EUR",
        "moneda_nombre": "Euro"
    },
    "Suiza": {
        "timezone": "Europe/Zurich",
        "idioma": "Alemán, Francés, Italiano",
        "dato_turistico": "Famosa por los Alpes y el chocolate.",
        "hemisferio": "Norte",
        "moneda_codigo": "CHF",
        "moneda_nombre": "Franco suizo"
    }
}
# Tasa para convertir de nuestra moneda base (ARS) a la moneda de referencia (USD)
# Este es un valor de ejemplo.
TASA_ARS_A_USD = 0.00084 # Ejemplo: 1 USD = ~1190 ARS

# Tasas de cambio de referencia. Usamos el dólar como base.
# La idea es: 1 USD = X de la moneda local.
TASAS_A_USD = {
    "ARS": 1190.48,
    "EUR": 0.85,
    "JPY": 144.88,
    "USD": 1.0,
    "CAD": 1.37,
    "MXN": 18.82,
    "BRL": 5.48,
    "COP": 4088.25,
    "CLP": 943.40,
    "PEN": 3.55,
    "GBP": 0.73,
    "CHF": 0.80
}