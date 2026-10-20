# Diapositiva 51: Resolucion DNS pasiva con socket
# Version robusta: resuelve una lista de dominios dentro de una funcion que
# devuelve la IP o None, de modo que un dominio invalido no tumbe el recorrido.

import socket  # modulo de red de la biblioteca estandar


def resolver(dominio: str) -> str | None:  # recibe un texto y devuelve texto o None
    """Devuelve la IP del dominio o None si no se puede resolver."""  # descripcion de la funcion
    try:  # intentamos la resolucion dentro de la funcion
        return socket.gethostbyname(dominio)  # si resuelve, devolvemos la IP
    except socket.gaierror:  # si el nombre no existe o falla la resolucion
        return None  # devolvemos None para avisar sin imprimir aqui


for dominio in ["scanme.nmap.org", "localhost", "dominio-que-no-existe.invalid"]:  # recorremos la lista
    ip = resolver(dominio)  # llamamos a la funcion con cada dominio
    print(f"[+] {dominio}: {ip}" if ip else f"[-] {dominio}: no resuelto")  # un mensaje segun haya IP o no
