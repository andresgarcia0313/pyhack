# Diapositiva 145: Script 1 - Banner grabbing con socket (version completa, partes 1 a 4)
# El libro parte este script en las diapositivas 142 a 145; aqui va integrado y funcional.
# Recorre siete puertos clasicos de un objetivo autorizado y muestra el banner de cada uno.

import socket  # modulo para conexiones de red


def capturar_banner(host: str, puerto: int, timeout: float = 3.0) -> str:  # funcion que devuelve el banner como texto
    try:  # protege contra errores de red (puerto cerrado, sin respuesta, etc.)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crea un socket TCP sobre IPv4
        sock.settimeout(timeout)  # limite de espera; evita que el programa se cuelgue
        sock.connect((host, puerto))  # abre la conexion al host y puerto
        try:  # el envio va en su propio try por si el servicio lo rechaza
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")  # estimulo minimo por si el puerto es web
        except Exception:  # si fallo el envio
            pass  # no importa: igual intentamos leer lo que el servicio ya mando
        banner = sock.recv(1024).decode("utf-8", errors="replace").strip()  # lee hasta 1024 bytes y pasa a texto
        sock.close()  # cierra la conexion
        return banner  # devuelve el banner limpio
    except socket.timeout:  # el servicio no respondio a tiempo
        return "[TIMEOUT] No se recibio respuesta"  # puerto probablemente filtrado por un firewall
    except ConnectionRefusedError:  # el host rechazo la conexion
        return "[CERRADO] Puerto no disponible"  # puerto cerrado activamente (no hay servicio)
    except Exception as e:  # cualquier otro error inesperado
        return f"[ERROR] {e}"  # devuelve el detalle del error


if __name__ == "__main__":  # solo se ejecuta si corremos este archivo directamente
    HOST_OBJETIVO = "scanme.nmap.org"  # objetivo autorizado (no una IP de terceros)
    PUERTOS = [21, 22, 25, 80, 110, 143, 443]  # lista de puertos clasicos a revisar
    print(f"{'Puerto':<10} {'Banner'}")  # encabezado de la tabla de resultados
    print("-" * 60)  # linea separadora de 60 guiones
    for puerto in PUERTOS:  # recorre cada puerto de la lista
        resultado = capturar_banner(HOST_OBJETIVO, puerto)  # captura el banner de ese puerto
        print(f"{puerto:<10} {resultado[:80]}")  # imprime el puerto y los primeros 80 caracteres del banner
# Salida tipica (puerto 22): 22    SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
