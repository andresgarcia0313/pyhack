# Diapositiva 190: Sesiones HTTP con requests.Session
# Muestra como una sesion guarda y reenvia sola la cookie de login,
# de modo que el servidor nos sigue reconociendo entre peticiones.

import requests  # libreria para enviar peticiones HTTP

session = requests.Session()                         # creamos un objeto que recuerda las cookies
session.get("http://127.0.0.1/login")                # GET inicial: obtiene cookies o token del formulario
session.post(
    "http://127.0.0.1/login",
    data={"username": "tester", "password": "password"},  # POST con las credenciales para autenticarnos
)
# La cookie de sesion se reenvia sola: el servidor nos reconoce.
response = session.get("http://127.0.0.1/profile")   # pedimos una zona protegida con la misma sesion
print(response.status_code)   # 200 si la sesion sigue activa (seguimos autenticados)
