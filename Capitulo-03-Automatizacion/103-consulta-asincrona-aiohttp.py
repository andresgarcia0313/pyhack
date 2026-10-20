# Diapositiva 103: Consultas asincronas con asyncio y aiohttp
# Muestra una corrutina que aplica el delay etico asincrono y hace un GET
# que no bloquea, capturando errores para no tumbar el lote.

# "asyncio" coordina las corrutinas; "aiohttp" pide sin bloquear; "random" da el jitter.
import asyncio, aiohttp, random

# Conector que limita a 5 el maximo de conexiones simultaneas.
CONECTOR = aiohttp.TCPConnector(limit=5)


# "async def" declara una corrutina: se ejecuta con await, no al llamarla.
async def consultar_async(session, url: str) -> dict:
    # "await" marca una pausa que cede el control; dormimos entre 0.5 y 1.5 s.
    await asyncio.sleep(random.uniform(0.5, 1.5))
    # "try" protege la peticion.
    try:
        # "async with" abre y cierra solo la respuesta; tope total de 8 s.
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=8)) as resp:
            # Devolvemos la URL y el codigo HTTP recibido.
            return {"url": url, "codigo": resp.status}
    # Capturamos cualquier error para que un fallo no detenga la recoleccion.
    except Exception as e:
        # Devolvemos el error como dato.
        return {"url": url, "error": str(e)}
