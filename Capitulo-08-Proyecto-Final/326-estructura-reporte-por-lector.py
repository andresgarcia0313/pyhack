# Diapositiva 326: Estructura de un reporte profesional
# Muestra las secciones tipicas de un reporte de pentest y a que lector
# apunta cada una: la direccion, el equipo tecnico o ambos.

# Lista de parejas: (titulo de la seccion, lector objetivo).
secciones = [
    ("Portada y metadatos", "ambos"),
    ("Resumen ejecutivo", "direccion"),
    ("Alcance y metodologia", "ambos"),
    ("Tabla de hallazgos por severidad", "ambos"),
    ("Detalle de cada hallazgo", "equipo tecnico"),
    ("Apendices con evidencia cruda", "equipo tecnico"),
]
# enumerate nos da un numero i que empieza en 1; desempaquetamos titulo y lector de cada pareja.
for i, (titulo, lector) in enumerate(secciones, start=1):
    # Mostramos el numero, el titulo y entre corchetes el lector al que apunta.
    print(f"{i}. {titulo}  [lector: {lector}]")
