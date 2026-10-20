# -*- coding: utf-8 -*-
# Diapositiva 232: SSH y Paramiko, vision general
# Muestra las tres fases de SSH y cuando encaja cada biblioteca.
# Requiere tener instalado Paramiko (pip install paramiko).

# Las tres fases de SSH ocurren, en orden, cada vez que te conectas.
FASES = ["negociacion de algoritmos", "autenticacion", "apertura de canales"]

# paramiko  -> un host, control fino (comandos, SFTP, tuneles)
# Fabric    -> muchos hosts, tareas repetitivas (construido sobre paramiko)
# AsyncSSH  -> muchas conexiones concurrentes (asyncio)

import paramiko  # biblioteca que implementa SSHv2 en Python puro

print("Version de Paramiko:", paramiko.__version__)  # muestra la version instalada
print("Fases de SSH:", FASES)  # muestra las tres fases
