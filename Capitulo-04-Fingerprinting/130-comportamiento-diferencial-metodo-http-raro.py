# Diapositiva 130: Senales que emiten los servicios
# Muestra el "comportamiento diferencial": se envia un verbo HTTP inventado
# y se observa como responde el servidor, porque el formato del error delata la implementacion.
# Uso autorizado: solo contra scanme.nmap.org o tu propio laboratorio.

import socket  # modulo de Python para abrir conexiones de red (sockets)


def metodo_raro(host: str, puerto: int = 80) -> str:  # define la funcion; host y puerto (80 por defecto)
    """Envia un verbo HTTP inexistente para ver como responde el servidor."""  # texto de ayuda de la funcion
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crea un socket TCP sobre IPv4
    s.settimeout(3.0)  # espera maximo 3 segundos; evita que el programa se cuelgue
    s.connect((host, puerto))  # abre la conexion al host y puerto indicados
    s.send(b"FAKEVERB / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")  # envia un metodo HTTP falso (bytes)
    datos = s.recv(1024).decode("utf-8", errors="replace")  # lee hasta 1024 bytes y los pasa a texto tolerante
    s.close()  # cierra la conexion para liberar recursos
    return datos.splitlines()[0] if datos else "[sin respuesta]"  # devuelve la primera linea, o un aviso si vino vacio


# Uso autorizado: contra scanme.nmap.org o tu propio laboratorio
print(metodo_raro("scanme.nmap.org"))  # llama la funcion e imprime la primera linea de la respuesta
# Salida tipica: 'HTTP/1.1 400 Bad Request'  (el formato del error delata la implementacion)
