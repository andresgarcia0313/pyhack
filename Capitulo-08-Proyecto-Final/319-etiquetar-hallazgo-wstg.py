# Diapositiva 319: OWASP, etiquetado de hallazgos en reportes Python
# Muestra como ponerle a un hallazgo el identificador de la prueba OWASP que
# lo encontro, usando el formato vigente WSTG v4.2 (no los viejos OTG).

# Diccionario que describe un hallazgo con su identificador WSTG.
hallazgo = {
    "id_wstg": "WSTG-INPV-01",   # Prueba de Cross Site Scripting reflejado
    "descripcion": "Parametro 'q' refleja la entrada sin sanitizar",
    "severidad": "Alta",
    "evidencia": "<script>alert(1)</script>",
    "url": "http://127.0.0.1:8080/buscar?q=<script>alert(1)</script>",  # entorno local de laboratorio
}

# Categorias WSTG v4.2 mas usadas en pruebas automatizadas:
# WSTG-INFO -> Recopilacion de informacion
# WSTG-ATHN -> Pruebas de autenticacion
# WSTG-INPV -> Pruebas de validacion de entrada (inyeccion SQL, XSS, etc.)
# Mostramos la severidad en mayusculas y el identificador de la prueba.
print(f"[{hallazgo['severidad'].upper()}] {hallazgo['id_wstg']}")
