# Diapositiva 292: Objetivo de negocio frente a objetivo tecnico
# Muestra como traducir una peticion vaga del cliente (objetivo de negocio)
# en una lista de objetivos tecnicos medibles y verificables.

# Guardamos en una variable el texto que suele decir el cliente en palabras de negocio.
objetivo_negocio = "Queremos saber si la banca en linea es vulnerable"

# Creamos una lista; cada elemento es un diccionario con la tecnica, los activos y el criterio de exito.
objetivos_tecnicos = [
    # Primer objetivo tecnico: un escaneo de puertos sobre 12 servidores.
    {"tecnica": "escaneo de puertos TCP", "activos": "anexo A (12 servidores)",
     "criterio_exito": "lista de puertos abiertos por servidor"},
    # Segundo objetivo tecnico: averiguar el producto y la version de cada servicio hallado.
    {"tecnica": "fingerprinting de servicios", "activos": "puertos abiertos hallados",
     "criterio_exito": "producto y version de cada servicio"},
    # Tercer objetivo tecnico: probar la autenticacion del portal web.
    {"tecnica": "pruebas de autenticacion web", "activos": "https://banca.lab/login",
     "criterio_exito": "resultado de 10 casos de WSTG-ATHN documentados"},
]

# Imprimimos el objetivo de negocio; la f delante del texto permite insertar variables con {}.
print(f"Negocio: {objetivo_negocio}")
# Recorremos la lista con enumerate para tener un numero i que empieza en 1.
for i, o in enumerate(objetivos_tecnicos, start=1):
    # Por cada objetivo mostramos su numero, su tecnica, sus activos y el criterio de exito.
    print(f"  T{i}. {o['tecnica']} sobre {o['activos']} -> {o['criterio_exito']}")
