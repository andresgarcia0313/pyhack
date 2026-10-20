# Diapositiva 176: 5.1 Fundamentos de HTTP y clientes en Python (introduccion)
# Muestra lo mas simple que se puede hacer: enviar una peticion HTTP
# y mirar que responde el servidor de laboratorio.

import requests  # trae la libreria "requests", la herramienta estrella para hablar HTTP

# Enviamos un GET (pedir una pagina) a nuestro servidor local de laboratorio.
# Nunca a un sitio de terceros sin autorizacion.
respuesta = requests.get("http://127.0.0.1")  # guardamos la respuesta en la variable "respuesta"

print("Codigo de estado:", respuesta.status_code)   # imprime el numero de resultado: 200 si todo va bien
print("Servidor:", respuesta.headers.get("Server"))  # imprime la cabecera "Server": dice que software corre el servidor
