# -*- coding: utf-8 -*-
# Diapositiva 236: Ejecucion remota de comandos con Paramiko
# Define una funcion que conecta por SSH y ejecuta una lista de comandos,
# capturando su salida. El cierre y el uso se ven en la diapositiva 237.
# Solo contra hosts autorizados.

import paramiko  # biblioteca SSH para Python

def ejecutar_comandos_remotos(host, usuario, contrasena, comandos):  # define la funcion
    resultados = {}  # diccionario donde guardaremos la salida de cada comando
    cliente = paramiko.SSHClient()  # crea el cliente SSH
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # politica de laboratorio
    try:  # intenta conectar y ejecutar
        cliente.connect(hostname=host, username=usuario,
                        password=contrasena, timeout=10)  # abre la conexion SSH
        print(f"[+] Conexion establecida con {host}")  # avisa que conecto
        for cmd in comandos:  # recorre cada comando de la lista
            # exec_command() ejecuta el comando y devuelve tres canales: entrada, salida y error.
            stdin, stdout, stderr = cliente.exec_command(cmd)  # 3 canales
            salida = stdout.read().decode("utf-8").strip()  # lee la salida normal como texto
            error = stderr.read().decode("utf-8").strip()   # lee los errores como texto
            # Guarda la salida normal o, si esta vacia, el mensaje de error.
            resultados[cmd] = salida if salida else error
    except paramiko.AuthenticationException:  # credenciales rechazadas
        print("[-] Fallo de autenticacion")
    # (el cierre y el return se completan en la diapositiva 237)
