# Diapositiva 167: Resultado del clasificador de servicios
# Muestra como aplicar el clasificador a una lista de servicios detectados con una
# comprension de lista. Incluye el clasificador (diapositivas 165 y 166) para ser ejecutable.

TIPOS_SERVICIO = {  # mapa puerto -> categoria (de la diapositiva 165)
    22: "Acceso remoto", 23: "Acceso remoto",
    21: "Transferencia de archivos", 445: "Transferencia de archivos",
    80: "Servicio web", 443: "Servicio web", 8080: "Servicio web",
    3306: "Base de datos", 5432: "Base de datos", 27017: "Base de datos",
    25: "Correo electronico", 389: "Directorio",
}
VERSIONES_RIESGO_ALTO = [  # lista negra de versiones riesgosas
    ("OpenSSH", "7.2"), ("Apache", "2.4.49"),
    ("nginx", "1.14.0"), ("vsftpd", "2.3.4"),
]


def clasificar_servicio(puerto: int, software: str, version: str) -> dict:  # clasificador de la diapositiva 166
    tipo = TIPOS_SERVICIO.get(puerto, "Desconocido")  # categoria por puerto
    riesgo = "Bajo"  # empezamos en bajo
    for sw, ver in VERSIONES_RIESGO_ALTO:  # recorre la lista negra
        if sw.lower() in software.lower() and ver in version:  # coincidencia insensible a mayusculas
            riesgo = "Alto"  # sube a alto
            break
    if riesgo == "Bajo" and version:  # heuristica de antiguedad
        partes = version.split(".")  # separa la version por puntos
        if partes and partes[0].isdigit() and int(partes[0]) < 2:  # numero mayor 0 o 1
            riesgo = "Medio"  # sube a medio
    return {"puerto": puerto, "tipo": tipo, "software": software,
            "version": version, "riesgo_preliminar": riesgo}


servicios_detectados = [  # lista de tuplas (puerto, software, version)
    (22, "OpenSSH", "7.2p2"),
    (80, "Apache", "2.4.41"),
    (3306, "MySQL", "8.0.27"),
]
inventario = [clasificar_servicio(p, sw, v) for p, sw, v in servicios_detectados]  # aplica la funcion a cada tupla
for item in inventario:  # recorre el inventario clasificado
    print(f"{item['software']:8s} {item['version']:8s} -> "  # imprime software y version alineados
          f"{item['tipo']:16s} / riesgo {item['riesgo_preliminar']}")  # y su tipo y riesgo
# OpenSSH  7.2p2    -> Acceso remoto    / riesgo Alto
# Apache   2.4.41   -> Servicio web     / riesgo Bajo
# MySQL    8.0.27   -> Base de datos    / riesgo Bajo
