# -*- coding: utf-8 -*-
# Diapositiva 228: SYN Scan, logica del half-open scan
# Explica como interpretar la respuesta de un SYN scan y genera un puerto de
# origen aleatorio con RandShort() para que el escaneo sea mas realista.

# Interpretacion de la respuesta de un SYN scan:
# resp con flags "SA" (SYN-ACK) -> ABIERTO (no enviamos ACK: queda a medio abrir)
# resp con flags "R"  (RST)     -> CERRADO
# sin respuesta (None)          -> FILTRADO (hay un firewall)

from scapy.all import TCP, RandShort  # TCP (clase) y RandShort (numero corto aleatorio)

# RandShort() da un numero aleatorio corto, ideal como puerto de origen variable.
sport = RandShort()  # puerto de origen aleatorio, mas realista que uno fijo

print("Puerto de origen aleatorio:", int(sport))  # int() lo convierte a numero entero para mostrarlo
