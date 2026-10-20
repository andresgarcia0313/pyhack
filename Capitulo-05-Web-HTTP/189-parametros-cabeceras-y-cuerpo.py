# Diapositiva 189: Parametros, cabeceras y cuerpo
# Muestra como enviar a la vez datos en la URL (params), metadatos
# (headers) y datos en el cuerpo (json) en una sola peticion.

import requests  # libreria para enviar peticiones HTTP

url = "http://127.0.0.1/api/recurso"   # recurso del laboratorio
response = requests.post(
    url,
    params={"debug": "true"},                 # query string: queda como ?debug=true en la URL
    headers={"Accept": "application/json"},    # cabecera: pedimos que nos respondan en JSON
    json={"username": "tester"},               # cuerpo enviado en formato JSON
)
print(response.status_code, response.url)   # mostramos el codigo y la URL final usada
# Mantener SIEMPRE las solicitudes dentro del alcance autorizado.
