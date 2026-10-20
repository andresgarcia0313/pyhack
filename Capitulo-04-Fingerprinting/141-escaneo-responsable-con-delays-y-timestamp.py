# Diapositiva 141: Consideraciones de seguridad operacional (OPSEC)
# Muestra un escaneo responsable: pausas entre conexiones para no disparar el IDS/IPS
# y registro de cada accion con su marca de tiempo para documentar el informe.

import socket  # conexiones de red
import time  # para hacer pausas (delays)
from datetime import datetime  # para obtener la fecha y hora actual


def escaneo_responsable(host: str, puertos: list, delay: float = 0.5) -> None:  # None: no devuelve valor, solo imprime
    """Escanea con delays y registra cada accion con timestamp (OPSEC)."""  # texto de ayuda
    for puerto in puertos:  # recorre la lista de puertos a revisar
        marca = datetime.now().isoformat(timespec="seconds")  # fecha y hora actual en formato estandar (segundos)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crea el socket TCP/IPv4
        s.settimeout(2.0)  # limite de 2 segundos de espera
        estado = "abierto" if s.connect_ex((host, puerto)) == 0 else "cerrado"  # connect_ex da 0 si conecto bien
        s.close()  # cierra el socket
        print(f"[{marca}] {host}:{puerto} -> {estado}")  # registra la accion con su timestamp
        time.sleep(delay)   # delay para no disparar el IDS/IPS


# Uso autorizado
escaneo_responsable("scanme.nmap.org", [22, 80], delay=0.5)  # revisa dos puertos con medio segundo de pausa
