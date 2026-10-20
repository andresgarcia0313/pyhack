# -*- coding: utf-8 -*-
# Diapositiva 220: Ciclo de vida de un socket
# Muestra, lado a lado, la secuencia de pasos del servidor y la del cliente.

# Lista con los pasos que sigue siempre un servidor, en orden.
SERVIDOR = ["socket()", "bind()", "listen()", "accept()", "recv()/send()", "close()"]

# Lista con los pasos que sigue siempre un cliente, en orden.
CLIENTE = ["socket()", "connect()", "send()/recv()", "close()"]

# El servidor se BLOQUEA (se detiene a esperar) en accept() hasta que llega un cliente.

for paso in SERVIDOR:        # recorre cada paso del ciclo del servidor
    print("servidor:", paso)  # imprime el paso actual
