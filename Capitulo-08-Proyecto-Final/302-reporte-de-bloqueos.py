# Diapositiva 302: Metricas de progreso en tiempo real, parte 2
# Muestra como avisar primero lo que importa: si hay tareas bloqueadas, se
# dice "SI, requiere atencion"; si no, se dice "No".

# Diccionario con un progreso de ejemplo: hay bloqueos y una tarea bloqueada.
progreso = {"porcentaje_completado": 25.0, "hay_bloqueos": True,
            "conteos": {"bloqueada": 1}}

# Condicional en una sola linea: si hay_bloqueos es True muestra el aviso, si no, "No".
print(f"Bloqueos: {'SI - requiere atencion' if progreso['hay_bloqueos'] else 'No'}")

# Si hay bloqueos, armamos un mensaje mas detallado para el correo diario al cliente.
if progreso["hay_bloqueos"]:
    print(f"Estado: {progreso['porcentaje_completado']}% con "
          f"{progreso['conteos']['bloqueada']} tarea(s) bloqueada(s). Se requiere apoyo del cliente.")
