# Diapositiva 96: ThreadPoolExecutor, parte 2
# Muestra como recoger resultados con as_completed: los futuros se procesan
# a medida que terminan, sin esperar a que acaben todos.

# "ThreadPoolExecutor" y "as_completed" vienen del modulo concurrent.futures.
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


# Funcion de la diapositiva 95: consulta un dominio y devuelve su estado.
def consultar_dominio(dominio: str) -> dict:
    try:
        r = requests.get(f"https://{dominio}", timeout=5)
        return {"dominio": dominio, "codigo": r.status_code}
    except requests.RequestException as e:
        return {"dominio": dominio, "error": str(e)}


# Lista de dominios de ejemplo.
dominios = ["example.com", "python.org", "github.com", "owasp.org"]
# Abrimos el pool de hilos con tope de concurrencia.
with ThreadPoolExecutor(max_workers=2) as executor:
    # Encolamos las tareas y asociamos cada futuro a su dominio.
    futuros = {executor.submit(consultar_dominio, d): d for d in dominios}
    # "as_completed" entrega cada futuro en cuanto su tarea termina.
    for futuro in as_completed(futuros):
        # "result()" obtiene el valor que devolvio la funcion.
        resultado = futuro.result()
        # Mostramos el resultado apenas llega.
        print(resultado)

# Salida (orden de finalizacion, no de lanzamiento):
# {'dominio': 'python.org', 'codigo': 200}
# {'dominio': 'example.com', 'codigo': 200} ...
