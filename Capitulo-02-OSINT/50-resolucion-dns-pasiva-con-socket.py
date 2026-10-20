# Diapositiva 50: Resolucion DNS pasiva con Python
# Muestra como traducir un nombre de dominio a su direccion IP consultando
# los servidores DNS del sistema, sin enviar ni un paquete al objetivo.

import socket  # modulo de la biblioteca estandar para operaciones de red

dominio = "scanme.nmap.org"  # dominio autorizado por Nmap para practicar
try:  # intentamos resolver; si algo falla, saltamos al bloque except
    ip_principal = socket.gethostbyname(dominio)  # pide la IP del dominio al DNS del sistema
    print(f"[+] Dominio:      {dominio}")  # mostramos el dominio consultado
    print(f"[+] IP principal: {ip_principal}")  # mostramos la IP obtenida
except socket.gaierror as e:  # se lanza si el nombre no se puede resolver
    print(f"[-] Error de resolucion: {e}")  # avisamos del error sin que el programa se caiga
