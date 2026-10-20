# Diapositiva 37: Estructuras anidadas, reconocimiento multi host (continuacion)
# Recorre la estructura anidada con dos for y arma un reporte legible, usando
# "or" para poner un texto por defecto cuando el banner es None.
# Se incluye aqui el diccionario del ejemplo anterior para que corra solo.

# Mismo diccionario anidado de la diapositiva 36 (resumido para que el archivo corra solo).
resultados = {
    "192.168.56.1": {
        "hostname": "router.lab",
        "puertos": {
            80: {"estado": "abierto", "banner": "Apache/2.4.41"},
            22: {"estado": "abierto", "banner": "OpenSSH_8.2"},
            23: {"estado": "filtrado", "banner": None},
        },
        "etiquetas": ["gateway", "prioridad_alta"],
    },
    "192.168.56.10": {
        "hostname": "servidor-web.lab",
        "puertos": {
            80: {"estado": "abierto", "banner": "nginx/1.18.0"},
            443: {"estado": "abierto", "banner": "nginx/1.18.0"},
        },
        "etiquetas": ["web", "produccion"],
    },
}

# for exterior: recorre cada host (IP y sus datos).
for ip, datos in resultados.items():
    # \n deja una linea en blanco antes de cada host para que el reporte respire.
    print(f"\n[HOST] {ip} ({datos['hostname']})")
    # for interior: recorre los puertos del host, ordenados por numero.
    for puerto, info in sorted(datos["puertos"].items()):
        # "or" devuelve "Sin banner" cuando el banner es None (o vacio).
        banner = info["banner"] or "Sin banner"
        # Imprime puerto, estado y banner con guion normal.
        print(f"  :{puerto} [{info['estado']}] - {banner}")
