# Diapositiva 149: Script 2 - Cabeceras HTTP con requests (version completa, partes 1 a 4)
# El libro parte este script en las diapositivas 146 a 149; aqui va integrado y funcional.
# Hace una peticion HEAD a un objetivo web y muestra las cabeceras utiles para fingerprinting.

import requests  # libreria comoda para peticiones HTTP/HTTPS
import urllib3  # libreria de bajo nivel que requests usa por debajo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # calla avisos de certificado; solo en laboratorio


def extraer_cabeceras_http(url: str) -> dict:  # devuelve un diccionario con las cabeceras encontradas
    cabeceras_de_interes = [  # lista curada de cabeceras que delatan tecnologia
        "Server", "X-Powered-By", "X-Generator", "X-AspNet-Version",
        "X-AspNetMvc-Version", "Via", "X-Cache", "Set-Cookie",
        "Content-Security-Policy", "Strict-Transport-Security",
    ]
    try:  # protege contra errores de conexion o de tiempo
        respuesta = requests.head(  # peticion HEAD: pide solo las cabeceras, no el cuerpo
            url, timeout=5, verify=False, allow_redirects=True,  # verify=False solo en laboratorio (cert. autofirmado)
            headers={"User-Agent": "Mozilla/5.0 (compatible; EthicalScanner/1.0)"},  # nos identificamos de forma honesta
        )
        print(f"\n[+] URL objetivo : {url}")  # muestra la URL consultada
        print(f"[+] Codigo HTTP  : {respuesta.status_code}")  # muestra el codigo de estado (200, 403, 404...)
        hallazgos = {}  # diccionario vacio donde guardaremos lo relevante
        for cabecera in cabeceras_de_interes:  # recorre la lista de cabeceras de interes
            valor = respuesta.headers.get(cabecera)  # .get devuelve None si la cabecera no vino (no falla)
            if valor:  # si la cabecera existe y tiene valor
                print(f"    {cabecera}: {valor}")  # la muestra en pantalla
                hallazgos[cabecera] = valor  # y la guarda en el diccionario
        return hallazgos  # devuelve siempre un diccionario (lleno si hubo exito)
    except requests.exceptions.ConnectionError:  # no se pudo conectar
        print(f"[-] No se pudo conectar a {url}")
        return {}  # devuelve diccionario vacio para no romper el codigo que llama
    except requests.exceptions.Timeout:  # la peticion tardo demasiado
        print(f"[-] Timeout al conectar a {url}")
        return {}  # tambien devuelve diccionario vacio


if __name__ == "__main__":  # solo corre si ejecutamos este archivo directamente
    URL_OBJETIVO = "http://127.0.0.1"  # laboratorio local (DVWA/Metasploitable)
    extraer_cabeceras_http(URL_OBJETIVO)  # llama la funcion con el objetivo propio
