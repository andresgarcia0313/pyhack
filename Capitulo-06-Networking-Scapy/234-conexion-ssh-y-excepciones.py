# -*- coding: utf-8 -*-
# Diapositiva 234: Conexion SSH, autenticacion y manejo de excepciones
# Muestra como conectar con Paramiko (por clave o por contrasena) y capturar
# el fallo de autenticacion. El resto de excepciones se ve en la diapositiva 235.
# Solo en laboratorio autorizado.

import paramiko, socket  # paramiko para SSH; socket aporta la excepcion de timeout

cliente = paramiko.SSHClient()  # crea el cliente SSH
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # politica de laboratorio

# Opcion segura: autenticar por clave privada RSA en vez de por contrasena.
# clave = paramiko.RSAKey.from_private_key_file("/ruta/a/id_rsa")  # carga la clave privada
# cliente.connect(hostname="192.168.56.101", username="pentest", pkey=clave)  # pkey = clave privada

try:  # intentamos conectar dentro de un try para manejar los errores posibles
    # connect() abre la conexion SSH; timeout=5 limita la espera a 5 segundos.
    cliente.connect(hostname="192.168.56.101", username="admin",
                    password="incorrecto", timeout=5)  # solo en lab autorizado
except paramiko.AuthenticationException:  # se dispara si las credenciales son rechazadas
    print("[-] Credenciales incorrectas")  # (mas excepciones en la diapositiva 235)
