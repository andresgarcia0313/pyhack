# -*- coding: utf-8 -*-
# Diapositiva 219: Cliente TCP minimo en Python
# Muestra el ciclo del cliente: crear socket, connect, recibir datos y cerrar.

import socket  # modulo de redes de Python

# Se crea el socket TCP sobre IPv4.
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect() establece la conexion con el servidor, que ya debe estar escuchando.
# 127.0.0.1 es "localhost": la propia maquina; el trafico no sale a ninguna red.
cliente.connect(("127.0.0.1", 9999))  # localhost: no sale a la red

# recv(1024) recibe hasta 1024 bytes (el tamano del buffer, no lo que llegara exacto).
respuesta = cliente.recv(1024)  # recibe hasta 1024 bytes

# .decode("utf-8") convierte los bytes recibidos en texto; .strip() quita saltos sobrantes.
print(f"[*] Respuesta: {respuesta.decode('utf-8').strip()}")  # muestra el texto recibido

cliente.close()  # cierra el socket del cliente
# Salida esperada: [*] Respuesta: Hola desde el servidor
