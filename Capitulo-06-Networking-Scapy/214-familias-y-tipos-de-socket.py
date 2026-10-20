# -*- coding: utf-8 -*-
# Diapositiva 214: Sockets en Python, conceptos fundamentales
# Muestra las combinaciones mas comunes de familia (IPv4/IPv6) y tipo (TCP/UDP)
# al crear un socket.

import socket  # modulo de redes de Python

# AF_INET = IPv4; SOCK_STREAM = TCP. Es la combinacion tipica de web y SSH.
tcp_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # socket TCP sobre IPv4

# SOCK_DGRAM = UDP: envia datagramas sueltos, sin conexion previa.
udp_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # socket UDP sobre IPv4

# AF_INET6 = IPv6: direcciones nuevas y mas largas.
tcp_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)  # socket TCP sobre IPv6

for s in (tcp_ipv4, udp_ipv4, tcp_ipv6):  # recorre los tres sockets creados
    s.close()                             # cierra cada uno para liberar el recurso

# Un cliente web comun sobre IPv4 usa AF_INET + SOCK_STREAM.
