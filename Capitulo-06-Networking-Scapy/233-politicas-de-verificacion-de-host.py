# -*- coding: utf-8 -*-
# Diapositiva 233: Politicas de verificacion de host en Paramiko
# Muestra como fijar la politica para hosts desconocidos: AutoAddPolicy en
# laboratorio (comoda pero insegura) y RejectPolicy en produccion (estricta).

import paramiko  # biblioteca SSH para Python

cliente = paramiko.SSHClient()  # crea el objeto cliente SSH

# En laboratorio: aceptar automaticamente hosts nuevos (comodo, pero inseguro).
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # agrega la clave sin verificar

# En produccion: cargar los hosts conocidos y RECHAZAR los desconocidos.
# cliente.load_system_host_keys()                               # carga el known_hosts del sistema
# cliente.set_missing_host_key_policy(paramiko.RejectPolicy())  # rechaza hosts no conocidos
