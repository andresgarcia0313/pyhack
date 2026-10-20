# Diapositiva 178: Estructura de una solicitud HTTP
# Muestra las tres partes de una peticion (linea, cabeceras y cuerpo)
# construyendo un POST de login contra el laboratorio.

import requests  # libreria para enviar peticiones HTTP

url = "http://127.0.0.1/login"   # direccion del recurso al que enviaremos el login

# Las cabeceras son metadatos: pares clave-valor que acompanan la peticion.
cabeceras = {
    "User-Agent": "Mozilla/5.0 (compatible; EthicalTester/1.0)",  # dice que tipo de cliente somos
    "Content-Type": "application/x-www-form-urlencoded",          # formato clasico de un formulario HTML
}

# El cuerpo (body) lleva los datos del formulario: usuario y contrasena.
cuerpo = {"username": "admin", "password": "secret"}   # el contenido que enviamos

# Enviamos un POST: metodo tipico para mandar datos como un login.
respuesta = requests.post(url, headers=cabeceras, data=cuerpo)   # data=... va en el cuerpo

print(respuesta.status_code)   # 200, o 302 si el login redirige a otra pagina
