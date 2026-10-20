# Diapositiva 303: El plan de trabajo como sistema vivo
# Muestra como un script actualiza el estado de una tarea en un archivo
# plan.json, de modo que el plan refleje siempre lo que de verdad paso.

# json convierte entre diccionarios de Python y texto en formato JSON.
import json
# Path facilita leer y escribir archivos sin tanto codigo.
from pathlib import Path

# Creamos un objeto que apunta al archivo plan.json.
ruta = Path("plan.json")
# Escribimos un plan inicial: una tarea en progreso. json.dumps lo convierte a texto.
ruta.write_text(json.dumps([{"id": "T-02", "estado": "en_progreso"}]), encoding="utf-8")


# Funcion que cambia el estado de una tarea identificada por su id.
def marcar(id_tarea: str, estado: str) -> None:
    # Leemos el archivo y lo convertimos de texto a lista de diccionarios.
    tareas = json.loads(ruta.read_text(encoding="utf-8"))
    # Recorremos las tareas buscando la que tenga el id indicado.
    for t in tareas:
        if t["id"] == id_tarea:
            # Cambiamos su estado al nuevo valor.
            t["estado"] = estado
    # Guardamos la lista actualizada; ensure_ascii=False conserva tildes, indent=2 la deja legible.
    ruta.write_text(json.dumps(tareas, ensure_ascii=False, indent=2), encoding="utf-8")


# Marcamos la tarea T-02 como completada (asi lo haria el script al terminar su trabajo).
marcar("T-02", "completada")      # lo llamaria banner_grabber.py al terminar
# Mostramos el contenido final del archivo.
print(ruta.read_text(encoding="utf-8"))
