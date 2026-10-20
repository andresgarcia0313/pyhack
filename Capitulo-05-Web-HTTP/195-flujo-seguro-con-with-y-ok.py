# Diapositiva 195: Automatizar un flujo HTTP de forma segura (codigo)
# Muestra el patron con dos detalles pulcros: 'with' para cerrar la
# sesion sola y '.ok' para verificar que el login salio bien.

import requests  # libreria para enviar peticiones HTTP

# 'with' cierra la sesion y libera conexiones automaticamente al salir del bloque.
with requests.Session() as session:
    login = session.post(
        "http://127.0.0.1/dvwa/login.php",
        data={"username": "tester", "password": "password"},   # credenciales del login
    )
    if login.ok:                       # .ok = True si el codigo de estado es menor que 400
        response = session.get("http://127.0.0.1/dvwa/index.php")  # accedemos al recurso protegido
        print(response.status_code)    # mostramos el codigo de estado
    else:
        print("[-] Login fallido:", login.status_code)   # avisamos si el login no funciono
