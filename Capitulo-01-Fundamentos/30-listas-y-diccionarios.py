# Diapositiva 30: Listas y diccionarios, objetivos y resultados
# Muestra la lista para la secuencia de objetivos y el diccionario para el
# resultado de un host, con acceso seguro usando .get().

# Lista de objetivos (texto); el orden importa y admite cambios.
objetivos = ["192.168.56.101", "192.168.56.102", "127.0.0.1"]
# .append agrega un objetivo al final de la lista.
objetivos.append("192.168.56.103")
# Recorre la lista e imprime cada IP.
for ip in objetivos:
    print(f"[*] Procesando objetivo: {ip}")

# Diccionario con el resultado estructurado de un host; cada clave es un campo.
resultado_escaneo = {
    "host": "192.168.56.101",
    "puertos_abiertos": [22, 80, 443],
    "sistema_operativo": "Linux",
    "tiempo_respuesta_ms": 12,
}
# .get("clave", "defecto") lee la clave y, si no existe, devuelve el valor por defecto (no falla).
so = resultado_escaneo.get("sistema_operativo", "Desconocido")
# La clave "version_ssh" no existe, asi que devuelve "no detectada".
ssh = resultado_escaneo.get("version_ssh", "no detectada")
# Muestra ambos valores.
print(f"[+] Sistema operativo detectado: {so} | SSH: {ssh}")

# Demuestra que con corchetes, una clave inexistente si lanza error.
try:
    # Acceso con corchetes a una clave que no existe: lanza KeyError.
    resultado_escaneo["version_ssh"]
# Atrapa el KeyError y muestra el mensaje.
except KeyError as e:
    print(f"[!] Con corchetes falla: KeyError {e}")
