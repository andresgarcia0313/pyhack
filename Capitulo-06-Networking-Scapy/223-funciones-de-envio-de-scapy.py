# -*- coding: utf-8 -*-
# Diapositiva 223: Conceptos clave de Scapy
# Resume las funciones de envio de Scapy y cuando se usa cada una.

# Mapa mental de las funciones de envio:
# send(pkt)       -> solo envia (capa 3), sin esperar respuesta
# sr(pkt)         -> envia y recibe VARIAS respuestas (capa 3)
# sr1(pkt)        -> envia y espera UNA respuesta (capa 3)
# sendp/srp/srp1  -> equivalentes en capa 2 (Ethernet, direcciones MAC)

# Guardamos en una variable la funcion adecuada para nuestro caso:
# un paquete IP del que esperamos una sola respuesta.
eleccion = "sr1"  # un paquete IP, una respuesta esperada

print("Funcion elegida:", eleccion)  # muestra la eleccion en pantalla
