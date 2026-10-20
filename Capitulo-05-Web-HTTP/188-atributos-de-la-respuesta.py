# Diapositiva 188: Construccion y analisis de una solicitud (codigo)
# Muestra los atributos principales del objeto respuesta: estado,
# cabeceras, texto y la URL final tras redirecciones.

import requests  # libreria para enviar peticiones HTTP

url = "http://127.0.0.1/test"     # direccion del recurso de laboratorio
response = requests.get(url)      # enviamos el GET y guardamos la respuesta
print(response.status_code)   # resultado HTTP: 200, 404, 500...
print(response.headers)       # diccionario con los metadatos de la respuesta
print(response.text[:80])     # primeros 80 caracteres del cuerpo (como texto)
# response.json()  -> usar solo si el Content-Type es application/json
print(response.url)           # URL final a la que se llego tras seguir redirecciones
# La respuesta trae lo suficiente para que el script decida el siguiente paso.
