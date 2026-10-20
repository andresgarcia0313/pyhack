# Diapositiva 320: OWASP, etiquetado de hallazgos en reportes Python, parte 2
# Muestra como imprimir, de forma legible y alineada, los detalles de un
# hallazgo: su descripcion, la URL y la evidencia.

# Reutilizamos el mismo diccionario de hallazgo de la diapositiva 319.
hallazgo = {
    "id_wstg": "WSTG-INPV-01",
    "descripcion": "Parametro 'q' refleja la entrada sin sanitizar",
    "severidad": "Alta",
    "evidencia": "<script>alert(1)</script>",
    "url": "http://127.0.0.1:8080/buscar?q=<script>alert(1)</script>",
}

# Imprimimos cada campo con su etiqueta alineada para que se lea como una ficha.
print(f"  Descripcion : {hallazgo['descripcion']}")
print(f"  URL         : {hallazgo['url']}")
print(f"  Evidencia   : {hallazgo['evidencia']}")
