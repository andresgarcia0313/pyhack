# Diapositiva 205: Prueba 3 - Enumeracion de directorios y archivos (parte 2, completa)
# Muestra la enumeracion completa: interpreta 200, 301/302 y otros
# codigos, maneja errores de red y pausa entre peticiones.

import time       # libreria para pausar entre peticiones
import requests  # libreria para enviar peticiones HTTP

# Estas dos lineas vienen de la diapositiva 199 (sesion ya autenticada en DVWA).
BASE_URL = "http://127.0.0.1/dvwa"   # direccion base del laboratorio
sesion = requests.Session()           # sesion que ya tendria la cookie de login

rutas_comunes = ["admin/", "backup/", "config/", "login.php", "robots.txt"]  # rutas a probar
print("[*] Iniciando enumeracion de directorios...")
for ruta in rutas_comunes:            # recorremos cada ruta
    url_objetivo = f"{BASE_URL}/{ruta}"   # armamos la URL completa
    try:                              # protegemos la peticion por si falla la red
        r = sesion.get(url_objetivo, timeout=5, allow_redirects=False)  # pedimos sin seguir redirecciones
        codigo = r.status_code        # guardamos el codigo de estado
        if codigo == 200:             # 200 = existe y es accesible
            print(f"  [200 ENCONTRADO]   {url_objetivo}")
        elif codigo in (301, 302):    # 301/302 = redireccion: la ruta existe pero manda a otro lado
            print(f"  [30x REDIRECCION]  {url_objetivo}")
        else:                         # cualquier otro codigo lo mostramos tal cual
            print(f"  [{codigo}]              {url_objetivo}")
    except requests.exceptions.RequestException as e:   # capturamos errores de red sin detener el barrido
        print(f"  [ERROR] {url_objetivo} - {e}")
    time.sleep(0.3)   # buena practica: pausa para no saturar el servidor (tecnica y etica)
