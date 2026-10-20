# -*- coding: utf-8 -*-
# Diapositiva 211: Introduccion a sockets y modelos cliente/servidor
# Muestra como se crea un socket (el "canal" de comunicacion) y como se cierra.
# Pensar en el socket como una linea telefonica: se abre, se usa y se cuelga.

import socket  # modulo estandar de Python para trabajar con redes

# socket.socket(familia, tipo) crea el canal, pero todavia no conecta con nadie.
# AF_INET = direcciones IPv4; SOCK_STREAM = conexion tipo TCP (confiable).
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # se crea el socket TCP sobre IPv4

print(type(s))  # muestra el tipo del objeto: <class 'socket.socket'>

s.close()  # cierra el socket, es decir, "cuelga la linea" y libera el recurso
