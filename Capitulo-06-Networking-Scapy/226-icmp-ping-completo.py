# -*- coding: utf-8 -*-
# Diapositiva 226: ICMP Ping, construir, enviar y analizar respuesta
# Junta todo en un ping artesanal con Scapy y analiza la respuesta.
# Solo en sistemas autorizados: el envio no autorizado puede ser ilegal (Ley 1273).

from scapy.all import IP, ICMP, sr1  # clases IP e ICMP y la funcion sr1

# ICMP() por defecto es un "echo request", el mensaje que pregunta "estas ahi?".
paquete = IP(dst="192.168.56.101") / ICMP()  # ICMP() por defecto = echo request

# Envia y espera una respuesta, con tope de 2 segundos y sin mensajes ruidosos.
respuesta = sr1(paquete, timeout=2, verbose=False)

if respuesta:  # si hubo respuesta, el host contesto
    print(f"[+] Host activo: {respuesta[IP].src}")   # IP de origen de la respuesta
    print(f"[+] TTL recibido: {respuesta[IP].ttl}")  # TTL recibido (pista del sistema operativo)
    respuesta.show()  # despliega el paquete recibido completo, para analisis detallado
else:
    print("[-] Sin respuesta (host inactivo o filtrado)")  # None: apagado o firewall
