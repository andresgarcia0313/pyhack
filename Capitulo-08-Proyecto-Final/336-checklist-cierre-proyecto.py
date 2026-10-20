# Diapositiva 336: Resumen del capitulo
# Muestra las cuatro ideas del capitulo como una lista de verificacion de
# cierre: el proyecto solo es "cerrable" si todas estan en True.

# Diccionario con las cuatro ideas; el valor dice si ya se cumplieron.
cierre = {
    "1. Planificacion con alcance y autorizacion firmada": True,
    "2. Controles y metodologia aplicados y registrados": True,
    "3. Tareas con criterios de exito y seguimiento": True,
    "4. Reporte entregado y evidencias cifradas y custodiadas": False,
}
# Juntamos las ideas que todavia estan en False (lo pendiente).
pendientes = [k for k, v in cierre.items() if not v]
# El proyecto es cerrable solo si la lista de pendientes esta vacia.
print("Proyecto cerrable:", not pendientes)
# Mostramos cada pendiente que quede.
for p in pendientes:
    print("  Falta:", p)
