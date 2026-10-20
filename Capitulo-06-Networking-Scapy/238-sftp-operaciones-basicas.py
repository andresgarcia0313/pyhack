# -*- coding: utf-8 -*-
# Diapositiva 238: SFTP y SCP, transferencia segura de archivos
# Resume las operaciones de SFTP, cuya interfaz se parece al modulo os de Python.

# SFTP expone una API parecida al modulo os:
# sftp.put(local, remoto)   -> subir un archivo
# sftp.get(remoto, local)   -> descargar un archivo
# sftp.listdir(ruta)        -> listar el contenido de una carpeta
# sftp.stat(ruta)           -> ver metadatos (tamano, permisos, fechas)
# sftp.mkdir / sftp.remove  -> crear carpeta / borrar archivo
# SFTP viaja sobre el canal SSH (puerto 22); NO es FTPS (que es FTP sobre TLS).

# Lista con los nombres de las operaciones basicas, solo para repaso.
operaciones = ["put", "get", "listdir", "stat", "mkdir", "remove"]

print("Operaciones SFTP:", operaciones)  # muestra la lista en pantalla
