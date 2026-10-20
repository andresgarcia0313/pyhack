# Diapositiva 338: Resultados esperados
# Muestra los criterios de aceptacion del laboratorio final como una lista
# comprobable; el rechazo de un objetivo fuera de alcance es el mas importante.

# Diccionario con cada criterio y la evidencia que lo demuestra.
resultados_esperados = {
    "paquete_importable": "import toolkit sin error",
    "cli_responde": "python -m toolkit.cli --help muestra la ayuda",
    "rechaza_fuera_de_alcance": "scan 8.8.8.8 -> [DENEGADO] y codigo 1",
    "tests_pasan": "pytest toolkit/tests/ -> todos PASSED",
    "reporte_generado": "report --formato markdown crea el archivo",
}
# Recorremos los criterios y los mostramos como casillas por marcar.
for criterio, evidencia in resultados_esperados.items():
    print(f"[ ] {criterio}: {evidencia}")
