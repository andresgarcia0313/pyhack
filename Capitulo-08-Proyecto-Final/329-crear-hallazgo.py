# Diapositiva 329: Campos minimos de un hallazgo individual
# Muestra una funcion que arma un hallazgo con todos sus campos minimos:
# id, titulo, fecha, CVSS, pasos, impacto, remediacion, estado y evidencias.

# datetime y timezone dan la fecha de deteccion en tiempo universal (UTC).
from datetime import datetime, timezone


# Funcion que recibe los datos y devuelve el hallazgo como diccionario.
def crear_hallazgo(id_hallazgo, titulo, cvss, descripcion,
                   pasos, impacto, remediacion) -> dict:
    return {
        "id": id_hallazgo,        # identificador unico, por ejemplo FIND-001
        "titulo": titulo,         # titulo descriptivo y especifico
        # Fecha de deteccion en UTC, en formato ISO y sin fracciones de segundo.
        "fecha_deteccion": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cvss_score": cvss,       # puntaje de severidad
        "pasos_reproduccion": pasos,   # lista de pasos para reproducir el hallazgo
        "impacto": impacto,       # que logra un atacante si lo explota
        "remediacion": remediacion,    # como corregirlo
        "estado": "Abierto",      # estado inicial del hallazgo
        "evidencias": [],         # lista vacia que luego se llena con archivos y hashes
    }


# Creamos un hallazgo de ejemplo con todos sus datos.
h = crear_hallazgo("FIND-001", "Inyeccion SQL en /login", 9.8,
                   "El parametro 'user' se concatena en la consulta",
                   ["Abrir /login", "Enviar user=' OR '1'='1 --"],
                   "Acceso a la tabla de usuarios sin credenciales",
                   "Consultas parametrizadas (CWE-89)")
# Mostramos algunos campos del hallazgo creado.
print(h["id"], "->", h["titulo"], "| CVSS", h["cvss_score"], "| estado", h["estado"])
