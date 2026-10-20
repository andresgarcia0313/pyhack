# Diapositiva 74: Requests con APIs REST, VirusTotal
# Consume la API REST de VirusTotal con requests, verificando el codigo de
# estado HTTP antes de leer el JSON y manejando los limites de tasa (429).

import os  # modulo para leer variables de entorno
import requests  # biblioteca para hacer peticiones HTTP

dominio = "example.com"  # dominio que vamos a consultar en VirusTotal
url = f"https://www.virustotal.com/api/v3/domains/{dominio}"  # armamos la URL del recurso del dominio
cabeceras = {"x-apikey": os.environ["VT_API_KEY"]}  # la clave de API va en la cabecera, tomada del entorno

respuesta = requests.get(url, headers=cabeceras, timeout=15)  # hacemos el GET con limite de 15 segundos
if respuesta.status_code == 200:  # 200 significa que la peticion fue exitosa
    stats = respuesta.json()["data"]["attributes"]["last_analysis_stats"]  # extraemos el conteo de detecciones
    print(f"Malicioso: {stats['malicious']}  Sospechoso: {stats['suspicious']}")  # mostramos las cifras clave
elif respuesta.status_code == 429:  # 429 significa que superamos el limite de peticiones
    print("[-] Limite de tasa superado (429). Espera y reintenta.")  # conviene esperar y reintentar
elif respuesta.status_code == 401:  # 401 significa que la clave no es valida
    print("[-] API key invalida (401).")  # avisamos del problema de credencial
else:  # cualquier otro codigo lo tratamos como error generico
    print(f"[-] Error: {respuesta.status_code}")  # mostramos el codigo recibido
