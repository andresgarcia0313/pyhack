# Diapositiva 34: Mini escaner, codigo completo (continuacion)
# Muestra como el mini lenguaje de formato de las f-strings alinea las columnas
# del reporte de puertos abiertos.

# Diccionario puerto -> servicio, incluyendo un puerto alto de cinco cifras.
reporte = {443: "HTTPS", 22: "SSH", 80: "HTTP", 49152: "Desconocido"}
# Encabezado del reporte.
print("[+] Reporte de puertos abiertos:")
# sorted(reporte.items()) ordena los pares por puerto (la clave).
for puerto, servicio in sorted(reporte.items()):
    # {puerto:5d} entero en ancho 5 alineado a la derecha; {servicio:<12} texto en ancho 12 a la izquierda.
    print(f"    Puerto {puerto:5d} -> {servicio:<12}|")
