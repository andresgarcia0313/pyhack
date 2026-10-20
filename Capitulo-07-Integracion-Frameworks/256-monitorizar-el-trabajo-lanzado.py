# Diapositiva 256: Configurar y ejecutar un modulo auxiliar, parte 2
# Muestra como monitorizar el trabajo lanzado: esperar unos segundos y consultar
# si el job_id sigue en la lista de trabajos activos de Metasploit.
# (Fragmento: usa "client" y "job_id" de las diapositivas anteriores.)

import time  # modulo del sistema para manejar pausas

time.sleep(5)  # esperamos 5 segundos para dar tiempo a que el escaneo avance
jobs_activos = client.jobs.list  # pedimos la lista de trabajos que siguen en ejecucion
if str(job_id) in jobs_activos:  # comprobamos si nuestro trabajo todavia aparece en la lista
    print(f"[*] El trabajo {job_id} sigue en ejecucion...")  # si esta, aun no termina
else:  # si ya no aparece en la lista
    print(f"[+] El trabajo {job_id} ha finalizado.")  # entonces el trabajo ya acabo
