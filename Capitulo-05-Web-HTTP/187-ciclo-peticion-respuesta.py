# Diapositiva 187: Construccion y analisis de una solicitud (flujo)
# Muestra el ciclo de 4 pasos: construir, enviar, el servidor procesa
# y analizar la respuesta para decidir que hacer.

import requests  # libreria para enviar peticiones HTTP

url = "http://127.0.0.1/test"          # paso 1: construimos la peticion (elegimos la URL)
respuesta = requests.get(url)          # paso 2: enviamos (paso 3: el servidor la procesa)
if respuesta.status_code == 200:       # paso 4: analizamos el resultado y decidimos
    # si fue exitoso, mostramos cuantos bytes de texto trajo la respuesta
    print("Recurso accesible, analizar contenido:", len(respuesta.text), "bytes")
