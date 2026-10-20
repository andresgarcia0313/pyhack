# Diapositiva 111: Formatos de almacenamiento, cuando usar cada uno
# Muestra una regla rapida para elegir el formato de guardado segun la
# necesidad: JSON/JSONL, CSV o SQLite.

# Regla de seleccion rapida:
# Jerarquias anidadas / auditoria linea a linea  -> JSON / JSONL
# Tabla simple para abrir en Excel               -> CSV
# Consultas, filtros y cruces frecuentes         -> SQLite

# Caso de ejemplo: necesitamos cruzar muchos registros por pais y puerto.
caso = "cruzar 300.000 registros por pais y puerto"
# Elegimos SQLite: SQL completo, archivo unico y sin servidor.
eleccion = "SQLite"
