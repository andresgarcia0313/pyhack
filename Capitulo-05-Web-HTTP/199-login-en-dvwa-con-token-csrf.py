# Diapositiva 199: Autenticacion previa: sesion activa con requests
# Muestra el patron GET-extraer-POST para iniciar sesion en DVWA, que
# exige un token CSRF que cambia en cada visita.

import requests  # libreria para enviar peticiones HTTP

BASE_URL = "http://127.0.0.1/dvwa"           # direccion base del laboratorio DVWA
LOGIN_URL = f"{BASE_URL}/login.php"          # URL del formulario de login
CREDENCIALES = {"username": "admin", "password": "password", "Login": "Login"}  # datos del login

sesion = requests.Session()   # creamos la sesion que guardara la cookie de autenticacion
# Obtener el token CSRF del formulario (cambia en cada visita).
respuesta_login = sesion.get(LOGIN_URL)   # GET inicial para traer el HTML del formulario
# Extraemos el token cortando el texto; es fragil, mejor usar BeautifulSoup.
token = respuesta_login.text.split("user_token' value='")[1].split("'")[0]
CREDENCIALES["user_token"] = token   # agregamos el token a los datos del login
# Login: la sesion guarda la cookie de autenticacion.
sesion.post(LOGIN_URL, data=CREDENCIALES)   # POST con credenciales + token
print("[+] Sesion iniciada correctamente")  # avisamos que el login se envio
