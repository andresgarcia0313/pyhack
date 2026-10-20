# Diapositiva 169: Campos minimos del inventario de activos (tabla)
# Muestra una entrada de inventario con todos los campos minimos que debe tener,
# incluido el banner_crudo, que es la evidencia verificable del hallazgo.

# Una entrada de inventario con todos los campos minimos
entrada = {  # diccionario con un activo documentado
    "host": "192.168.56.101", "puerto": 22, "protocolo": "TCP",  # a quien, que puerto y que protocolo
    "estado": "abierto", "tipo_servicio": "Acceso remoto",  # estado del puerto y categoria del servicio
    "software": "OpenSSH", "version": "7.2p2",  # software detectado y su version
    "banner_crudo": "SSH-2.0-OpenSSH_7.2p2 Ubuntu",   # evidencia verificable (texto original, sin modificar)
    "riesgo_preliminar": "Alto",  # nivel de riesgo asignado
    "notas": "Version con enumeracion de usuarios conocida",  # observaciones del analista
}
# Se puede volcar a JSON, exportar a CSV o insertar en SQLite segun la escala
print(len(entrada), "campos registrados")   # cuenta las claves del diccionario: 9 campos
