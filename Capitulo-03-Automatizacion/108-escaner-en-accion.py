# Diapositiva 108: Herramienta completa en accion
# Muestra la orquestacion con ThreadPoolExecutor: lanza las verificaciones
# en paralelo e imprime cada subdominio activo en cuanto termina.

# El pool de hilos y as_completed coordinan las tareas.
from concurrent.futures import ThreadPoolExecutor, as_completed

# Numero maximo de hilos simultaneos.
MAX_HILOS = 3


# Marcador de la funcion de las diapositivas 106 y 107.
def verificar_subdominio(subdominio: str) -> dict:
    # En el ejemplo real hace el GET con semaforo, delay y backoff.
    return {"subdominio": subdominio, "activo": True, "codigo": 200, "titulo": "Inicio"}


# Lista de subdominios propios a verificar.
subdominios = ["www.ejemplo.com", "mail.ejemplo.com", "vpn.ejemplo.com"]
# Abrimos el pool con el tope de hilos y lo cerramos solo al terminar.
with ThreadPoolExecutor(max_workers=MAX_HILOS) as ex:
    # Encolamos una tarea por subdominio y guardamos sus futuros.
    futuros = [ex.submit(verificar_subdominio, s) for s in subdominios]
    # Procesamos cada futuro apenas su tarea termina (resultados en tiempo real).
    for f in as_completed(futuros):
        # Obtenemos el diccionario que devolvio la funcion.
        r = f.result()
        # Si el subdominio esta activo, lo mostramos con su codigo y titulo.
        if r.get("activo"):
            print(f"[+] {r['subdominio']} ({r['codigo']}) -> {r.get('titulo','')}")
