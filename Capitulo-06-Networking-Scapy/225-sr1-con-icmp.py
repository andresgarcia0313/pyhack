# -*- coding: utf-8 -*-
# Diapositiva 225: Envio y recepcion, sr1() con ICMP
# Muestra como enviar un paquete y recoger una sola respuesta con sr1(),
# usando timeout para no colgarse. Solo contra hosts de laboratorio autorizados.

from scapy.all import IP, ICMP, sr1  # IP e ICMP (clases) y sr1 (enviar y esperar 1 respuesta)

# Se construye el paquete ICMP (ping) hacia el host de laboratorio.
paquete = IP(dst="192.168.56.101") / ICMP()  # host de laboratorio

# sr1() envia el paquete y espera una respuesta. timeout=2 = espera maximo 2 segundos.
# verbose=False silencia los mensajes automaticos de Scapy.
respuesta = sr1(paquete, timeout=2, verbose=False)  # espera max 2 s

if respuesta:  # comprobar siempre que hubo respuesta (si no, respuesta es None)
    # respuesta[IP].src = IP de origen; respuesta[IP].ttl = tiempo de vida recibido.
    print(f"[+] Host activo: {respuesta[IP].src}  TTL={respuesta[IP].ttl}")
else:
    print("[-] Sin respuesta (host inactivo o filtrado)")  # None: apagado o con firewall
