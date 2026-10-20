# Diapositiva 184: Solicitud HTTP manual con sockets (parte 2, codigo completo)
# Muestra la peticion manual completa: armar el texto, enviarlo en bytes
# y recibir la respuesta en un bucle hasta que el servidor cierre.

import socket  # libreria para manejar conexiones de red a bajo nivel

host = "scanme.nmap.org"   # objetivo autorizado para practicar
puerto = 80                # puerto estandar de HTTP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket TCP sobre IPv4
cliente.connect((host, puerto))   # abrimos la conexion al servidor

# Armamos el texto de la peticion; cada linea termina en \r\n.
solicitud = (
    "GET / HTTP/1.1\r\n"          # linea de solicitud
    f"Host: {host}\r\n"           # cabecera Host, obligatoria
    "Connection: close\r\n"       # pedir cierre al terminar
    "\r\n"                         # linea en blanco: fin de cabeceras
)
cliente.send(solicitud.encode())          # send requiere bytes, por eso encode()
respuesta = b""                            # acumulador vacio de bytes
while True:                                # bucle para recibir por fragmentos
    fragmento = cliente.recv(4096)        # trae lo disponible, hasta 4096 bytes
    if not fragmento:                     # bytes vacios = el servidor cerro
        break                             # salimos del bucle
    respuesta += fragmento                # acumulamos todos los fragmentos
cliente.close()                            # cerramos la conexion
lineas = respuesta.decode(errors="replace").split("\r\n")  # pasamos bytes a texto y partimos por lineas
for linea in lineas[:20]:                 # mostramos solo las primeras 20 lineas (cabeceras)
    print(linea)
# Salida tipica: HTTP/1.1 200 OK / Server: Apache/... / Content-Type: text/html ...
