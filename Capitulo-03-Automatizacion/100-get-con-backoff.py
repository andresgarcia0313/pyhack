# Diapositiva 100: Implementando retroceso exponencial en Python
# Muestra la funcion get_con_backoff: ante un 429 (demasiadas peticiones)
# espera un tiempo creciente y reintenta con "continue".

# "time" aplica la pausa; "requests" hace la peticion.
import time, requests


# Funcion que hace un GET y reintenta ante errores temporales.
def get_con_backoff(url: str, max_reintentos: int = 5):
    # Texto de documentacion de la funcion.
    """GET con retroceso exponencial ante 429. Espera 1,2,4,8,16 s."""
    # Damos un numero fijo de oportunidades, del intento 0 al max-1.
    for intento in range(max_reintentos):
        # "try" protege la parte que puede fallar por red.
        try:
            # Hacemos el GET con tope de 10 segundos.
            respuesta = requests.get(url, timeout=10)
            # Si el servidor pide calma con un 429...
            if respuesta.status_code == 429:
                # ...calculamos la espera creciente (1, 2, 4, 8, 16 s).
                espera = 2 ** intento
                # Informamos que esperaremos.
                print(f"[429] Limite alcanzado. Esperando {espera}s...")
                # Dormimos el tiempo calculado.
                time.sleep(espera)
                # "continue" salta al siguiente intento sin ejecutar el resto.
                continue
            # Si no fue 429, devolvemos la respuesta (continua en la parte 2).
            return respuesta
        # Si no se pudo conectar, se maneja en la diapositiva 101.
        except requests.ConnectionError:
            pass
