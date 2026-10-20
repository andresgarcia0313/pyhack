# -*- coding: utf-8 -*-
# Diapositiva 227: Flags TCP en Scapy
# Muestra los flags TCP como letras y construye un SYN hacia un puerto.
# Los flags son bits de control que indican la intencion del paquete.

# Diccionario que traduce cada letra de flag a su significado.
FLAGS = {"S": "SYN (inicio)", "A": "ACK (confirmacion)", "R": "RST (reinicio)",
         "F": "FIN (cierre)", "P": "PSH (push)", "U": "URG (urgente)"}

from scapy.all import IP, TCP  # clases IP y TCP

# flags="S" activa el flag SYN: es una peticion para iniciar una conexion.
syn = IP(dst="192.168.56.101") / TCP(dport=22, flags="S")  # peticion de conexion al puerto 22

print(syn.summary())  # muestra el paquete SYN construido
# Puerto abierto -> responde "SA" (SYN-ACK); cerrado -> "RA"/"R" (RST).
