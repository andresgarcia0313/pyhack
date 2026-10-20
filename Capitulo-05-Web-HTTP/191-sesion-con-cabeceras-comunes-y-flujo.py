# Diapositiva 191: Sesiones HTTP con requests.Session (ventajas)
# Muestra como definir cabeceras comunes una sola vez y reproducir un
# flujo de varias etapas que depende del estado acumulado.

import requests  # libreria para enviar peticiones HTTP

session = requests.Session()   # creamos la sesion que recordara cookies y cabeceras
# Cabeceras comunes definidas UNA vez para todas las peticiones de la sesion.
session.headers.update({"User-Agent": "EthicalTester/1.0"})

# Flujo de varias etapas que depende del estado acumulado (estar logueado).
session.post("http://127.0.0.1/login", data={"username": "t", "password": "p"})  # 1: iniciar sesion
session.get("http://127.0.0.1/carrito/agregar?id=5")   # 2: agregar un item (requiere estar logueado)
resumen = session.get("http://127.0.0.1/carrito")       # 3: ver el carrito con el item agregado
print(resumen.status_code)   # mostramos el codigo de estado del ultimo paso
