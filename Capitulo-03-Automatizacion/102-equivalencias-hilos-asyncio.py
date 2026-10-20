# Diapositiva 102: asyncio + aiohttp, concurrencia de alta escala
# Muestra las equivalencias mentales entre el modelo de hilos y el modelo
# asincrono, para trasladar lo ya aprendido a asyncio.

# Equivalencias mentales entre los dos modelos:
# ThreadPoolExecutor(max_workers=5)  <->  TCPConnector(limit=5)
# as_completed(futuros)              <->  asyncio.gather(*tareas)
# time.sleep(x)  (bloqueante)        <->  await asyncio.sleep(x)  (cede control)
# requests.get() (bloqueante)        <->  await session.get()     (no bloquea)

# Nota: en asyncio nunca se usa codigo bloqueante (requests, time.sleep),
# porque congelaria el bucle de eventos y se perderia la concurrencia.
