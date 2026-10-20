# Diapositiva 104: Consultas asincronas con asyncio y aiohttp (parte 2)
# Muestra el ensamblado: una sesion compartida, una tarea por URL y
# asyncio.gather para lanzarlas todas y recolectar resultados en orden.

# "asyncio" coordina; "aiohttp" hace las peticiones; "random" da el jitter.
import asyncio, aiohttp, random

# Conector que limita a 5 el maximo de conexiones simultaneas.
CONECTOR = aiohttp.TCPConnector(limit=5)


# Corrutina de la diapositiva 103: consulta una URL sin bloquear.
async def consultar_async(session, url: str) -> dict:
    await asyncio.sleep(random.uniform(0.5, 1.5))
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=8)) as resp:
            return {"url": url, "codigo": resp.status}
    except Exception as e:
        return {"url": url, "error": str(e)}


# Corrutina principal que orquesta todas las consultas.
async def main(urls: list[str]) -> None:
    # Abrimos una sola sesion que reutiliza conexiones (eficiente).
    async with aiohttp.ClientSession(connector=CONECTOR) as session:
        # Creamos una corrutina por URL (aun no se ejecutan).
        tareas = [consultar_async(session, u) for u in urls]
        # "gather" lanza todas y espera; el "*" desempaqueta la lista.
        resultados = await asyncio.gather(*tareas)
        # Recorremos los resultados (en el orden de las tareas) y los mostramos.
        for r in resultados:
            print(r)


# Lista de URLs de ejemplo a consultar.
urls_objetivo = ["https://python.org", "https://owasp.org", "https://github.com"]
# "asyncio.run" crea el bucle de eventos, corre main y lo cierra: punto de entrada unico.
asyncio.run(main(urls_objetivo))

# Salida: {'url': 'https://python.org', 'codigo': 200} ...
