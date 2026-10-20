# Diapositiva 115: Funcion normalize_record, puerto, texto y tags
# Muestra la receta repetida: tomar el valor (con alias), convertir el tipo,
# limpiar y poner None o lista vacia cuando no hay nada util.

# Suponemos un record en construccion y un raw de ejemplo.
record = {}
raw = {"port": "53", "target": "Ejemplo.com", "tags": "dns, publico"}

# Aceptamos "port" o "port_number" para el puerto.
port_raw = raw.get("port") or raw.get("port_number")
# "try" protege la conversion a entero, que falla si el texto no es numerico.
try:
    # Forzamos el puerto a entero; si no vino, lo dejamos en None.
    record["port"] = int(port_raw) if port_raw is not None else None
# Si no se pudo convertir (texto no numerico o tipo raro), queda en None.
except (ValueError, TypeError):
    record["port"] = None
# Objetivo: texto limpio y en minusculas, o None si queda vacio.
record["target"]  = str(raw.get("target", "")).strip().lower() or None
# Servicio: acepta tambien el alias "proto"; limpio y en minusculas.
record["service"] = str(raw.get("service", raw.get("proto", ""))).strip().lower() or None
# Banner: acepta el alias "data"; se limpia pero se conserva como viene.
record["banner"]  = str(raw.get("banner", raw.get("data", ""))).strip() or None
# Pais: acepta "country_code"; en mayusculas y recortado a dos letras (ISO).
record["country"] = str(raw.get("country_code", raw.get("country", ""))).upper()[:2] or None
# Tomamos las tags crudas; por defecto lista vacia.
tags_raw = raw.get("tags", [])
# Si las tags vienen como texto separado por comas, las partimos en lista.
if isinstance(tags_raw, str):
    # Partimos por coma, limpiamos cada etiqueta y descartamos las vacias.
    record["tags"] = [t.strip() for t in tags_raw.split(",") if t.strip()]
