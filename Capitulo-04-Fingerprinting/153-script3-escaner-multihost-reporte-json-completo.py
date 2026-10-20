# Diapositiva 153: Script 3 - Escaner multi-host con reporte JSON (version completa, partes 1 a 2 de las diapositivas 150 a 153)
# Junta socket y requests: captura banners y cabeceras de varios hosts y puertos,
# y guarda todo en un archivo JSON con marca de tiempo para el informe.

import socket, requests, json  # red de bajo nivel, HTTP comodo y manejo de JSON
from datetime import datetime  # fecha y hora para la trazabilidad
import urllib3  # libreria base de requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # calla avisos de certificado; solo en laboratorio


def banner_grabbing_completo(hosts: list, puertos: list) -> list:  # devuelve una lista de diccionarios (un activo por puerto)
    resultados = []  # lista vacia donde acumulamos cada hallazgo
    for host in hosts:  # recorre cada host de la lista
        for puerto in puertos:  # y por cada host, recorre cada puerto
            entrada = {  # diccionario con los campos fijos de este hallazgo
                "timestamp": datetime.utcnow().isoformat(),  # momento exacto de captura (trazabilidad)
                "host": host, "puerto": puerto,  # a quien y a que puerto consultamos
                "banner": "", "cabeceras_http": {},  # se llenaran mas abajo
            }
            try:  # protege la parte de socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket TCP/IPv4
                sock.settimeout(2.0)  # limite de 2 segundos
                sock.connect((host, puerto))  # abre la conexion
                if puerto in [80, 443, 8080, 8443]:  # puertos web: hay que estimular
                    # 'Host' es obligatorio por el virtual hosting
                    sock.send(b"HEAD / HTTP/1.0\r\nHost: " + host.encode() + b"\r\n\r\n")  # peticion HTTP minima
                banner_raw = sock.recv(2048).decode("utf-8", errors="replace").strip()  # lee hasta 2048 bytes y pasa a texto
                entrada["banner"] = banner_raw[:500]  # guardamos hasta 500 chars (no truncamos tanto como en la vista)
                sock.close()  # cierra el socket
            except Exception as e:  # si algo fallo en el socket
                entrada["banner"] = f"[ERROR] {str(e)}"  # deja el error registrado en el banner
            if puerto in [80, 443, 8080, 8443]:  # para puertos web, ademas pedimos cabeceras con requests
                esquema = "https" if puerto in [443, 8443] else "http"  # elige http o https segun el puerto
                try:
                    resp = requests.head(f"{esquema}://{host}:{puerto}",  # peticion HEAD
                        timeout=3, verify=False, allow_redirects=True)  # verify=False solo en laboratorio
                    entrada["cabeceras_http"] = dict(resp.headers)  # guarda las cabeceras ya parseadas
                except Exception:
                    pass  # si falla, al menos queda el banner del socket
            resultados.append(entrada)  # agrega este hallazgo a la lista
            print(f"[*] {host}:{puerto} -> {entrada['banner'][:60]}")  # muestra el avance (primeros 60 chars)
    return resultados  # devuelve la lista completa


if __name__ == "__main__":  # solo corre si ejecutamos este archivo directamente
    # Objetivos de laboratorio propio; nunca IPs de terceros sin autorizacion
    datos = banner_grabbing_completo(["127.0.0.1"], [21, 22, 80, 443, 8080])  # escanea localhost en esos puertos
    nombre = f"banners_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"  # nombre con fecha y hora (no sobreescribe)
    with open(nombre, "w", encoding="utf-8") as f:  # abre el archivo para escribir en UTF-8
        json.dump(datos, f, indent=2, ensure_ascii=False)  # vuelca el JSON legible y con tildes correctas
    print(f"[+] Reporte guardado en: {nombre}")  # confirma donde quedo el reporte
# Salida: [+] Reporte guardado en: banners_20241115_143200.json
