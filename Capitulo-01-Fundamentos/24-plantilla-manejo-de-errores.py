# Diapositiva 24: Manejo de excepciones, estructura completa
# La plantilla convertida en codigo real: lee una lista de objetivos desde un
# archivo usando try / except (varios tipos) / else / finally.

# Path maneja rutas y archivos; time mide tiempos.
from pathlib import Path
import time


# Recibe la ruta del archivo (texto) y devuelve una lista de textos.
def cargar_objetivos(ruta: str) -> list[str]:
    # Guarda el instante inicial para medir cuanto tarda.
    inicio = time.perf_counter()
    # Lista vacia donde se guardaran los objetivos leidos.
    objetivos: list[str] = []
    # Intenta leer el archivo, que puede no existir.
    try:
        # Lee todo el contenido del archivo como texto.
        texto = Path(ruta).read_text(encoding="utf-8")
    # El archivo no existe; e.filename trae su nombre.
    except FileNotFoundError as e:
        print(f"[ERROR] {e.filename} no existe")
    # Varios errores con la misma respuesta: la tupla (A, B) atrapa cualquiera de los dos.
    except (PermissionError, IsADirectoryError) as e:
        print(f"[ADVERTENCIA] No se pudo leer: {e}")
    # Corre solo si la lectura tuvo exito.
    else:
        # splitlines() parte por lineas; .strip() limpia cada una; el if descarta las vacias.
        objetivos = [l.strip() for l in texto.splitlines() if l.strip()]
        print(f"[OK] {len(objetivos)} objetivos cargados")
    # Corre siempre: muestra el tiempo con cuatro decimales (.4f).
    finally:
        print(f"[*] Tiempo: {time.perf_counter() - inicio:.4f} s")
    # Devuelve la lista (puede estar vacia si hubo error).
    return objetivos


# Crea un archivo de prueba con dos objetivos y una linea en blanco.
Path("objetivos.txt").write_text("127.0.0.1\nscanme.nmap.org\n\n")
# Caso exitoso: el archivo existe.
print(cargar_objetivos("objetivos.txt"))
# Caso de error: el archivo no existe.
print(cargar_objetivos("no_existe.txt"))
