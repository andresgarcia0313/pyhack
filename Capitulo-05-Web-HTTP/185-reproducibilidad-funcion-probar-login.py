# Diapositiva 185: 5.2 Uso de requests, sesiones y manejo de cookies (introduccion)
# Muestra la reproducibilidad: una funcion que prueba un login y se
# puede ejecutar identica cuantas veces se quiera.

import requests  # libreria para enviar peticiones HTTP

# Definimos una funcion que recibe usuario y clave y devuelve el codigo de estado.
# "usuario: str" y "clave: str" indican que esperamos texto; "-> int" que devuelve un numero.
def probar_login(usuario: str, clave: str) -> int:
    r = requests.post("http://127.0.0.1/dvwa/login.php",     # enviamos un POST al login
                      data={"username": usuario, "password": clave})  # datos del formulario
    return r.status_code   # devolvemos el codigo de estado de la respuesta

# Llamamos a la funcion con credenciales de prueba; se puede repetir identica mil veces.
print(probar_login("admin", "password"))   # imprime el codigo que devolvio el login
