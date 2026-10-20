# Diapositiva 255: Configurar y ejecutar un modulo auxiliar
# Muestra como cargar un modulo de escaneo SMB, ver sus opciones obligatorias,
# configurarlo con la IP del objetivo autorizado y ejecutarlo guardando el job_id.
# (Fragmento: usa el "client" creado en la diapositiva 253.)

# 3. Cargar el modulo auxiliar de escaneo SMB
modulo = client.modules.use("auxiliary", "scanner/smb/smb_version")  # cargamos el modulo por su tipo y nombre

print("\n[*] Opciones requeridas del modulo:")  # anunciamos la lista de opciones obligatorias
for nombre, detalles in modulo.required.items():  # recorremos cada opcion obligatoria y su descripcion
    print(f"    {nombre}: {detalles}")  # mostramos el nombre de la opcion y sus detalles

# 4. Configurar opciones (IP del objetivo AUTORIZADO del laboratorio)
modulo["RHOSTS"] = "192.168.56.101"   # IP de Metasploitable 2 en la red aislada del laboratorio
modulo["THREADS"] = 4  # cantidad de hilos de escaneo en paralelo
print("\n[+] Opciones configuradas correctamente")  # confirmamos que las opciones quedaron puestas

# 5. Ejecutar (auxiliar: sin payload)
trabajo = modulo.execute(payload="")  # lanzamos el modulo; un auxiliar no necesita payload
job_id = trabajo.get("job_id", None)  # obtenemos el identificador del trabajo lanzado (o None si no vino)
print(f"[+] Modulo ejecutado. Job ID: {job_id}")  # mostramos el job_id para poder monitorearlo luego
