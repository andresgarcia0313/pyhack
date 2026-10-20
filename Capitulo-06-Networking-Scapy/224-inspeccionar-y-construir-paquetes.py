# -*- coding: utf-8 -*-
# Diapositiva 224: Instalacion, inspeccion y construccion de paquetes
# Muestra como inspeccionar los campos de un protocolo con ls() y construir
# un paquete ICMP (ping) hacia un host de laboratorio. Requiere privilegios (sudo).

from scapy.all import IP, ICMP, ls  # IP e ICMP son clases; ls lista los campos de un protocolo

# ls(ICMP) muestra todos los campos de ICMP y sus valores por defecto (type, code, ...).
ls(ICMP)  # util cuando no se recuerda el nombre exacto de un campo

# Se construye un paquete apilando una capa IP con una capa ICMP (ping) hacia el laboratorio.
paquete = IP(dst="192.168.56.101") / ICMP()  # paquete ICMP (ping) hacia un host de laboratorio

paquete.show()             # .show() despliega todas las capas y campos, asignados e inferidos
print(paquete.summary())   # .summary() da la vista compacta de una linea
