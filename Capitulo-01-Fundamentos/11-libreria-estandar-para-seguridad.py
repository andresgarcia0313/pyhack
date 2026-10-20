# Diapositiva 11: 1.1 Introduccion a entorno y sintaxis de Python
# Muestra cuatro modulos de la biblioteca estandar utiles en seguridad,
# sin instalar nada extra: hashlib, ipaddress, json y socket.

# "import" trae modulos ya incluidos en Python para poder usarlos.
import hashlib, ipaddress, json, socket

# hashlib.sha256 calcula una huella del texto en bytes (la "b" marca bytes); .hexdigest() la vuelve texto y [:16] toma 16 caracteres.
print(hashlib.sha256(b"evidencia").hexdigest()[:16])     # huella de integridad
# ipaddress.ip_address crea un objeto IP; .is_private dice si es una IP de red privada.
print(ipaddress.ip_address("192.168.1.10").is_private)    # ¿IP privada?
# json.dumps convierte un diccionario de Python en texto JSON para intercambiar datos.
print(json.dumps({"puerto": 22, "estado": "abierto"}))    # formato de intercambio
# socket.gethostbyname traduce un nombre a su direccion IP (resolucion de nombres).
print(socket.gethostbyname("localhost"))                  # resolucion de nombres
