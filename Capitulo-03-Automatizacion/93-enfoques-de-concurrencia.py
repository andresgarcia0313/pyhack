# Diapositiva 93: Enfoques de concurrencia en Python
# Muestra la regla practica para elegir enfoque: hilos o asyncio para
# tareas de red (I/O), y multiprocessing para tareas de calculo (CPU).

# Regla practica de seleccion segun el tipo de tarea.
# Tarea de RED (esperar al servidor) -> threading o asyncio.
# Tarea de CALCULO (hash, cifrado masivo) -> multiprocessing.

# Guardamos en texto la descripcion de la tarea de ejemplo.
tarea = "descargar 200 URLs"
# Como el cuello de botella es esperar la red, elegimos I/O.
enfoque = "threading o asyncio"  # porque es I/O bound

# Un hash de 10 GB de datos seria CPU bound -> multiprocessing.
