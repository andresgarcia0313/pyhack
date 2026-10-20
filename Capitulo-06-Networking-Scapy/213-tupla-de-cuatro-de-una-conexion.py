# -*- coding: utf-8 -*-
# Diapositiva 213: Actores del modelo cliente/servidor
# Muestra la "tupla de cuatro" (IP y puerto de origen + IP y puerto de destino)
# que identifica de forma unica cada conexion en la red.

import socket  # modulo de redes de Python

# Se crea el socket TCP sobre IPv4 (aun sin conectar).
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect() inicia la conexion hacia un destino (IP o nombre, y puerto).
# scanme.nmap.org es un host que Nmap ofrece publicamente para practicar.
s.connect(("scanme.nmap.org", 80))  # se conecta al puerto 80 (web) del destino

print("Origen:", s.getsockname())   # getsockname() da (IP_origen, puerto_origen) de nuestra maquina
print("Destino:", s.getpeername())  # getpeername() da (IP_destino, puerto_destino) del servidor

s.close()  # cierra la conexion y libera el socket
# Las 4 cifras (2 de origen + 2 de destino) juntas hacen que la conexion sea unica.
