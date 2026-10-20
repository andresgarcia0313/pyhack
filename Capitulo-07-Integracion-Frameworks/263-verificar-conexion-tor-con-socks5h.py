# Diapositiva 263: Script, verificar conexion TOR con socks5h://
# Muestra como confirmar que el trafico sale realmente por TOR consultando
# el servicio oficial check.torproject.org a traves del proxy SOCKS5.

import requests  # biblioteca para hacer peticiones HTTP

proxies = {  # diccionario que le dice a requests que envie todo por TOR
    "http":  "socks5h://127.0.0.1:9050",   # socks5h: el DNS tambien viaja por TOR
    "https": "socks5h://127.0.0.1:9050",  # mismo proxy para las peticiones HTTPS
}

def verificar_tor() -> None:  # funcion que confirma si estamos usando TOR; no devuelve nada
    """Confirma que el trafico sale por TOR."""  # texto de ayuda que describe la funcion
    try:  # intentamos la peticion y capturamos posibles errores de conexion
        respuesta = requests.get(  # hacemos una peticion GET al servicio de verificacion
            "https://check.torproject.org/api/ip",  # endpoint que responde si tu salida es un nodo TOR
            proxies=proxies,  # usamos el diccionario de proxys definido arriba
            timeout=30,   # TOR es lento: damos un plazo generoso antes de rendirnos
        )
        datos = respuesta.json()  # convertimos la respuesta JSON en un diccionario de Python
        if datos.get("IsTor"):  # si el campo IsTor es verdadero, salimos por TOR
            print(f"[+] Trafico por TOR. IP de salida: {datos['IP']}")  # mostramos la IP de salida de TOR
        else:  # si IsTor es falso, el trafico no paso por TOR
            print(f"[-] ADVERTENCIA: no se usa TOR. IP real: {datos['IP']}")  # avisamos que se ve la IP real
    except requests.exceptions.ConnectionError:  # error que ocurre si TOR no esta corriendo
        print("[!] No se pudo conectar. Verifica que el servicio TOR esta activo.")  # pista para arreglarlo

verificar_tor()  # llamamos a la funcion para ejecutar la verificacion
