# Diapositiva 166: Clasificador de servicios por tipo y riesgo (version completa, diapositivas 165 y 166)
# Muestra un clasificador que asigna tipo (por puerto) y riesgo (por version conocida
# o por antiguedad). Incluye las tablas de la diapositiva 165 para que sea ejecutable.

TIPOS_SERVICIO = {  # mapa puerto -> categoria de servicio (de la diapositiva 165)
    22: "Acceso remoto", 23: "Acceso remoto",
    21: "Transferencia de archivos", 445: "Transferencia de archivos",
    80: "Servicio web", 443: "Servicio web", 8080: "Servicio web",
    3306: "Base de datos", 5432: "Base de datos", 27017: "Base de datos",
    25: "Correo electronico", 389: "Directorio",
}
VERSIONES_RIESGO_ALTO = [  # "lista negra" de versiones famosas por sus vulnerabilidades
    ("OpenSSH", "7.2"), ("Apache", "2.4.49"),
    ("nginx", "1.14.0"), ("vsftpd", "2.3.4"),
]


def clasificar_servicio(puerto: int, software: str, version: str) -> dict:  # devuelve un diccionario clasificado
    tipo = TIPOS_SERVICIO.get(puerto, "Desconocido")  # busca la categoria por puerto
    riesgo = "Bajo"  # conservador: empezamos en bajo y solo subimos con razon concreta
    for sw, ver in VERSIONES_RIESGO_ALTO:  # recorre la lista negra
        if sw.lower() in software.lower() and ver in version:  # comparacion insensible a mayusculas
            riesgo = "Alto"  # coincide con una version riesgosa: riesgo alto
            break  # ya encontramos, salimos del bucle
    if riesgo == "Bajo" and version:  # heuristica de antiguedad (solo si sigue en bajo y hay version)
        partes = version.split(".")  # parte "1.3.5" en ["1","3","5"]
        if partes and partes[0].isdigit() and int(partes[0]) < 2:  # si el numero mayor es 0 o 1
            riesgo = "Medio"  # sube a medio por sospecha de software muy antiguo
    return {"puerto": puerto, "tipo": tipo, "software": software,  # resultado estructurado
            "version": version, "riesgo_preliminar": riesgo}


print(clasificar_servicio(22, "OpenSSH", "7.2p2"))  # prueba con un OpenSSH de la lista negra
# {'puerto': 22, 'tipo': 'Acceso remoto', 'software': 'OpenSSH',
#  'version': '7.2p2', 'riesgo_preliminar': 'Alto'}
