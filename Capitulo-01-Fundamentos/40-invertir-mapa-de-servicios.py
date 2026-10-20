# Diapositiva 40: Comprensiones aplicadas a resultados de escaneo (continuacion)
# Muestra una comprension de diccionario (puerto -> servicio) y la inversion
# segura con defaultdict para no perder datos cuando se repite un servicio.
# Se incluye la lista del ejemplo anterior para que corra solo.

# defaultdict crea valores por defecto automaticamente (aqui, listas vacias).
from collections import defaultdict

# Misma lista de diccionarios de la diapositiva 39 (para que el archivo corra solo).
todos_puertos = [
    {"puerto": 22,   "estado": "abierto",  "servicio": "SSH"},
    {"puerto": 80,   "estado": "abierto",  "servicio": "HTTP"},
    {"puerto": 8080, "estado": "filtrado", "servicio": "HTTP-Alt"},
    {"puerto": 443,  "estado": "abierto",  "servicio": "HTTPS"},
    {"puerto": 23,   "estado": "cerrado",  "servicio": "Telnet"},
]

# Comprension de diccionario: {puerto: servicio} solo de los puertos abiertos.
mapa_servicios = {p["puerto"]: p["servicio"] for p in todos_puertos if p["estado"] == "abierto"}
# Muestra el mapa de servicios activos.
print(f"[+] Servicios activos: {mapa_servicios}")

# defaultdict(list): si la clave no existe, arranca con una lista vacia.
por_servicio: defaultdict[str, list[int]] = defaultdict(list)
# Recorre pares (puerto, servicio), incluyendo dos puertos con el mismo servicio.
for puerto, servicio in [(80, "HTTP"), (8000, "HTTP"), (22, "SSH")]:
    # .append agrega el puerto a la lista de ese servicio, sin perder los anteriores.
    por_servicio[servicio].append(puerto)
# dict(...) lo convierte en diccionario normal para mostrarlo.
print(dict(por_servicio))
