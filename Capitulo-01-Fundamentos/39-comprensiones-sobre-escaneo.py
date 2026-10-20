# Diapositiva 39: Comprensiones aplicadas a resultados de escaneo
# Muestra varias comprensiones sobre una lista de diccionarios (datos
# tabulares), como filtros de una hoja de calculo.

# Lista de diccionarios: cada uno es una "fila" con puerto, estado y servicio.
todos_puertos = [
    {"puerto": 22,   "estado": "abierto",  "servicio": "SSH"},
    {"puerto": 80,   "estado": "abierto",  "servicio": "HTTP"},
    {"puerto": 8080, "estado": "filtrado", "servicio": "HTTP-Alt"},
    {"puerto": 443,  "estado": "abierto",  "servicio": "HTTPS"},
    {"puerto": 23,   "estado": "cerrado",  "servicio": "Telnet"},
]
# Comprension: numeros de los puertos cuyo estado es "abierto".
puertos_abiertos = [p["puerto"] for p in todos_puertos if p["estado"] == "abierto"]
# Comprension con condicion de conjunto: puertos a revisar (abiertos o filtrados).
a_revisar = [p["puerto"] for p in todos_puertos if p["estado"] in {"abierto", "filtrado"}]
# Comprension de conjunto: los estados distintos que aparecen.
estados = {p["estado"] for p in todos_puertos}
# Muestra los puertos abiertos.
print(f"[+] Puertos abiertos: {puertos_abiertos}")
# Muestra los puertos a revisar, ordenados.
print(f"[+] A revisar: {sorted(a_revisar)}")
# Muestra los estados distintos, ordenados.
print(f"[+] Estados distintos: {sorted(estados)}")
