# Diapositiva 301: Metricas de progreso en tiempo real
# Muestra como contar las tareas por estado, calcular el porcentaje de avance
# y avisar si hay bloqueos, sin fallar cuando el plan esta vacio.

# Reutilizamos el dataclass y el plan definidos en la diapositiva 300.
from importlib import import_module
_m = import_module("300-dataclass-tarea-hacking-plan")
TareaHacking = _m.TareaHacking
plan = _m.plan


# Funcion que recibe la lista de tareas y devuelve un resumen con las metricas.
def calcular_progreso(tareas: list[TareaHacking]) -> dict:
    """Conteos por estado y porcentaje de avance."""
    # Empezamos un contador en cero para cada estado posible.
    conteos = {"pendiente": 0, "en_progreso": 0, "completada": 0, "bloqueada": 0}
    # Recorremos las tareas y sumamos 1 al contador del estado de cada una.
    for t in tareas:
        conteos[t.estado] += 1
    # total es la cantidad de tareas que hay.
    total = len(tareas)
    # Porcentaje de completadas; si total es 0 devolvemos 0 para no dividir por cero.
    porcentaje = conteos["completada"] / total * 100 if total > 0 else 0
    # Devolvemos un diccionario que otros scripts pueden usar.
    return {
        "total_tareas": total,
        "conteos": conteos,
        "porcentaje_completado": round(porcentaje, 1),   # redondeado a un decimal
        "hay_bloqueos": conteos["bloqueada"] > 0,         # True si hay al menos un bloqueo
    }


# Calculamos el progreso del plan de ejemplo.
progreso = calcular_progreso(plan)
# Mostramos solo el porcentaje completado.
print(f"Progreso: {progreso['porcentaje_completado']}%")
