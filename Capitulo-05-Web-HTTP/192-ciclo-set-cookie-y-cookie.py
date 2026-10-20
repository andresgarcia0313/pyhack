# Diapositiva 192: Cookies: estado entre solicitudes
# Muestra el ciclo de la cookie: el servidor la fija con Set-Cookie y
# la sesion la devuelve sola en la siguiente peticion.

import requests  # libreria para enviar peticiones HTTP

# Ver el ciclo Set-Cookie (el servidor fija) -> Cookie (el cliente devuelve).
session = requests.Session()                  # creamos la sesion que guarda cookies
r1 = session.get("http://127.0.0.1/login")    # primera peticion: el servidor responde con Set-Cookie
print("El servidor fijo:", r1.headers.get("Set-Cookie"))  # mostramos la cookie que nos dio
# En la siguiente peticion, la sesion reenvia esa cookie automaticamente.
r2 = session.get("http://127.0.0.1/")         # segunda peticion: ya llevamos la cookie guardada
print("Cookies que tengo:", session.cookies.get_dict())   # mostramos las cookies como diccionario
