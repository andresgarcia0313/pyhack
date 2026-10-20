# -*- coding: utf-8 -*-
# Diapositiva 222: Scapy, conceptos fundamentales
# Muestra como se apilan capas con el operador "/" para construir un paquete.
# Requiere tener instalado Scapy (pip install scapy).

from scapy.all import IP, TCP  # cada protocolo es una clase: IP y TCP

# El operador "/" apila capas de menor a mayor nivel: primero IP, dentro TCP.
# dst = destino; dport = puerto destino; flags="S" = bandera SYN (inicio de conexion).
paquete = IP(dst="192.168.56.101") / TCP(dport=80, flags="S")  # paquete IP que contiene un segmento TCP

# dst, dport y flags son atributos (campos) del paquete. Scapy calcula solo
# los checksums y las longitudes, asi que solo definimos lo importante.
print(paquete.summary())  # .summary() da una vista compacta de una linea del paquete
