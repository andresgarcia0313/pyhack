# Diapositiva 194: Automatizar un flujo HTTP de forma segura (patron)
# Muestra el esqueleto de 5 pasos: crear sesion, autenticarse, mantener
# estado, solicitar el recurso y validar la respuesta.

import requests  # libreria para enviar peticiones HTTP

# El patron de 5 pasos como esqueleto.
session = requests.Session()                                    # 1. crear la sesion
login = session.post("http://127.0.0.1/dvwa/login.php",
                     data={"username": "admin", "password": "password"})  # 2. autenticarse
# 3. mantener el estado: seguimos usando el mismo objeto 'session'.
perfil = session.get("http://127.0.0.1/dvwa/index.php")         # 4. solicitar el recurso protegido
if "Welcome" in perfil.text or perfil.url.endswith("index.php"):# 5. VALIDAR que si entramos
    print("[+] Autenticacion confirmada")
else:
    print("[-] La autenticacion fallo, revisar credenciales o token")
