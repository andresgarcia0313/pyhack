# -*- coding: utf-8 -*-
# Diapositiva 215: TCP vs UDP en hacking etico
# Resume en un diccionario las diferencias entre TCP (confiable) y UDP (rapido).

# TCP (SOCK_STREAM): handshake, entrega y orden garantizados -> escaneo, banners
# UDP (SOCK_DGRAM):  sin conexion, mas rapido, sin garantias  -> DNS, fuzzing
# Si se necesita confiabilidad absoluta, se elige TCP.

# Un diccionario guarda pares "clave: valor". Aqui cada caracteristica (clave)
# apunta a otro diccionario que compara TCP contra UDP.
tabla = {
    "orientado_a_conexion": {"TCP": True,  "UDP": False},   # TCP acuerda antes de enviar; UDP no
    "garantia_entrega":     {"TCP": True,  "UDP": False},   # TCP reenvia lo perdido; UDP no
    "orden_garantizado":    {"TCP": True,  "UDP": False},   # TCP ordena lo que llega; UDP no
    "velocidad":            {"TCP": "menor", "UDP": "mayor"},  # UDP es mas rapido por no verificar
}

print(tabla)  # muestra la tabla comparativa completa en pantalla
