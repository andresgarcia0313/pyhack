# Diapositiva 179: Metodos HTTP: relevancia en seguridad
# Muestra como el metodo OPTIONS revela que metodos acepta el
# servidor, dato util en la fase de reconocimiento.

import requests  # libreria para enviar peticiones HTTP

url = "http://127.0.0.1/api/recurso"   # recurso del laboratorio que vamos a consultar

# OPTIONS pregunta al servidor "que metodos permites sobre este recurso".
respuesta = requests.options(url)   # enviamos la peticion OPTIONS

# La respuesta trae la cabecera "Allow" con la lista de metodos permitidos.
# Si no viene, usamos el texto "no informado" como valor por defecto.
metodos_permitidos = respuesta.headers.get("Allow", "no informado")

print("Metodos permitidos:", metodos_permitidos)   # mostramos lo que acepta el servidor
# Ejemplo de salida: Metodos permitidos: GET, POST, PUT, DELETE, OPTIONS
# -> si PUT y DELETE estan activos, revisar si tienen control de acceso adecuado
