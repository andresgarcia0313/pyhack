# Diapositiva 327: Criterios de calidad de un reporte profesional
# Muestra los seis criterios que distinguen un buen reporte y un detalle
# breve de lo que exige cada uno.

# Diccionario donde la clave es el criterio y el valor es su exigencia concreta.
criterios = {
    "Reproducibilidad": "pasos exactos y comandos",
    "Severidad": "CVSS 3.1 con vector",
    "Evidencia": "capturas, logs, salidas con hash",
    "Remediacion": "accion concreta (p. ej. consultas parametrizadas)",
    "Trazabilidad": "CVE / CWE / OWASP",
    "Confidencialidad": "clasificacion y cifrado en reposo y transito",
}
# Recorremos las parejas clave-valor y las mostramos como una lista con guion.
for criterio, detalle in criterios.items():
    print(f"- {criterio}: {detalle}")
