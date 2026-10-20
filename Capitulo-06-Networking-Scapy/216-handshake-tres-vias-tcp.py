# -*- coding: utf-8 -*-
# Diapositiva 216: Handshake de tres vias TCP
# Describe en texto los tres mensajes del handshake y los posibles estados
# que revela un SYN scan.

# El handshake en palabras (mas adelante se construye con Scapy):
# 1. Cliente -> Servidor : SYN            ("quiero conectarme")
# 2. Servidor -> Cliente : SYN-ACK        ("de acuerdo, confirma")
# 3. Cliente -> Servidor : ACK            ("confirmado, conexion abierta")
# SYN scan: hace el paso 1 y recibe el 2, pero NO envia el 3 -> puerto abierto, menos rastro.

# Diccionario que asocia la respuesta recibida con el estado del puerto.
estados = {"SYN-ACK recibido": "puerto ABIERTO", "RST recibido": "puerto CERRADO"}

print(estados)  # muestra la relacion entre respuesta y estado del puerto
