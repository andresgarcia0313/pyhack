# Diapositiva 136: Banner grabbing - vision general
# Muestra el patron minimo del banner grabbing activo: conectar, (estimular) y leer.
# Uso autorizado: scanme.nmap.org puerto 22 (SSH, que habla solo).

# Patron minimo de banner grabbing activo: conectar -> (estimular) -> leer
import socket  # modulo para conexiones de red


def banner_basico(host: str, puerto: int) -> str:  # funcion que devuelve el banner como texto
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crea un socket TCP sobre IPv4
    s.settimeout(3.0)  # limite de 3 segundos de espera
    try:  # bloque protegido: pase lo que pase, al final cerramos el socket
        s.connect((host, puerto))  # abre la conexion
        return s.recv(1024).decode("utf-8", errors="replace").strip()  # lee, pasa a texto y quita espacios/saltos
    finally:  # se ejecuta siempre, haya exito o error
        s.close()  # cierra la conexion para no dejarla abierta


# Objetivo autorizado: scanme.nmap.org puerto 22 (SSH habla solo)
print(banner_basico("scanme.nmap.org", 22))  # llama la funcion e imprime el banner recibido
# Salida tipica: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
