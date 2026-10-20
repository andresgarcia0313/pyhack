# Diapositiva 36: Estructuras anidadas, reconocimiento multi host
# Muestra un diccionario anidado de reconocimiento de dos hosts y consultas
# utiles sobre el (prioritarios, con nginx, total de puertos abiertos).

# Diccionario anidado: cada IP tiene hostname, puertos (con estado y banner) y etiquetas.
resultados = {
    "192.168.56.1": {
        "hostname": "router.lab",
        "puertos": {
            80: {"estado": "abierto", "banner": "Apache/2.4.41"},
            22: {"estado": "abierto", "banner": "OpenSSH_8.2"},
            # banner None significa "no hay dato", distinto de un texto vacio.
            23: {"estado": "filtrado", "banner": None},
        },
        # etiquetas es una lista porque un host puede tener varios roles.
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

# Comprension de lista: las IP cuyas etiquetas incluyen "prioridad_alta".
prioritarios = [ip for ip, d in resultados.items() if "prioridad_alta" in d["etiquetas"]]
# Comprension de conjunto con dos for: IP cuyo banner empieza por "nginx"; (info["banner"] or "") evita fallar con None.
con_nginx = {ip for ip, d in resultados.items()
             for info in d["puertos"].values() if (info["banner"] or "").startswith("nginx")}
# sum con un generador: cuenta 1 por cada puerto en estado "abierto" en todos los hosts.
total_abiertos = sum(1 for d in resultados.values()
                     for info in d["puertos"].values() if info["estado"] == "abierto")
# Muestra los tres resultados.
print(prioritarios, con_nginx, total_abiertos)
