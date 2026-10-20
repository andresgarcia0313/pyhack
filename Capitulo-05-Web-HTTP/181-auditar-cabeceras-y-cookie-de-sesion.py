# Diapositiva 181: Cabeceras de respuesta: mina de informacion
# Muestra como auditar la seguridad de la cookie de sesion y la
# presencia de cabeceras de proteccion en la respuesta.

import requests  # libreria para enviar peticiones HTTP

# Pedimos la pagina de login del laboratorio y guardamos la respuesta.
r = requests.get("http://127.0.0.1/login")

# Leemos la cabecera "Set-Cookie"; si no viene, usamos texto vacio.
set_cookie = r.headers.get("Set-Cookie", "")

# Si la cookie NO incluye el atributo HttpOnly, es un hallazgo de seguridad.
if "HttpOnly" not in set_cookie:
    print("[HALLAZGO] Cookie sin HttpOnly: vulnerable a robo via XSS")

# Si la respuesta NO trae la cabecera Content-Security-Policy, la defensa XSS es debil.
if "Content-Security-Policy" not in r.headers:
    print("[HALLAZGO] Falta Content-Security-Policy: defensa XSS debil")
