# Diapositiva 186: Vision general del concepto
# Muestra en una sola peticion varias capacidades de requests:
# enviar parametros, autenticacion e inspeccionar la respuesta.

import requests  # libreria para enviar peticiones HTTP

# Enviamos un GET combinando parametros de URL y una cabecera de autenticacion.
r = requests.get("http://127.0.0.1/pagina",
                 params={"id": 1},                       # parametros que van en la URL (?id=1)
                 headers={"Authorization": "Bearer XYZ"}) # autenticacion mediante token Bearer

print("Estado :", r.status_code)              # inspeccionamos el codigo de estado
print("Tipo   :", r.headers.get("Content-Type"))  # leemos el tipo de contenido de la respuesta
print("Texto  :", r.text[:60])                # mostramos los primeros 60 caracteres del cuerpo
