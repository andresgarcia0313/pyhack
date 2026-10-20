# Diapositiva 193: Cookies: inspeccion con requests
# Muestra como listar las cookies de una sesion y recorrerlas una por
# una; el nombre suele delatar la tecnologia del servidor.

import requests  # libreria para enviar peticiones HTTP

session = requests.Session()           # creamos la sesion que guardara las cookies
session.get("http://127.0.0.1/")       # una peticion para que el servidor nos entregue cookies
print(session.cookies)                  # imprime todas las cookies de la sesion de golpe
for cookie in session.cookies:          # recorremos cada cookie una por una
    print(cookie.name, cookie.value)    # mostramos nombre y valor; el nombre delata la tecnologia
# Ejemplo: PHPSESSID 7f3a...  -> indica un backend hecho en PHP
