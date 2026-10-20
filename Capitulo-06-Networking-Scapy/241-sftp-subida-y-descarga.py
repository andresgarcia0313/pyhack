# -*- coding: utf-8 -*-
# Diapositiva 241: SFTP en accion, subida y descarga
# Ejemplo directo: conectar, subir un archivo con put() y descargar otro con get().
# Solo en el marco de un ejercicio autorizado (laboratorio aislado).

import paramiko  # biblioteca SSH/SFTP para Python

cliente = paramiko.SSHClient()  # crea el cliente SSH
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # politica de laboratorio

# connect() abre la conexion SSH con el host de laboratorio.
cliente.connect("192.168.56.101", username="auditor", password="P@ssw0rd")

sftp = cliente.open_sftp()  # abre el canal SFTP sobre la sesion SSH

sftp.put("./audit.sh", "/tmp/audit.sh")         # sube la herramienta (local -> remoto)
sftp.get("/etc/hostname", "./hostname_remoto")  # descarga evidencia (remoto -> local)

sftp.close()     # cierra el canal SFTP
cliente.close()  # cierra la conexion SSH
# En un pentest autorizado, la descarga demuestra el riesgo real de los datos.
