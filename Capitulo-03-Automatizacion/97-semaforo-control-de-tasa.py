# Diapositiva 97: Semaforos, control fino de tasa de peticiones
# Muestra un semaforo como "torniquete": deja pasar solo a un numero fijo
# de hilos al recurso a la vez, con un delay dentro de cada hilo.

# "threading" trae el semaforo; "requests" pide; "time" pausa; "random" da azar.
import threading, requests, time, random

# Semaforo que permite maximo 3 peticiones simultaneas.
semaforo = threading.Semaphore(3)


# Funcion que pide una URL respetando el limite del semaforo.
def peticion_controlada(url: str) -> None:
    # "with semaforo" adquiere un cupo al entrar y lo libera al salir del bloque.
    with semaforo:
        # "try" protege la parte que puede fallar por red.
        try:
            # Hacemos el GET con tope de 5 segundos.
            r = requests.get(url, timeout=5)
            # Mostramos el codigo HTTP y la URL.
            print(f"[{r.status_code}] {url}")
        # Si falla la peticion, capturamos el error de requests.
        except requests.RequestException as e:
            # Informamos el error sin romper el programa.
            print(f"[ERROR] {url}: {e}")
        # "finally" se ejecuta pase lo que pase (exito o error).
        finally:
            # Delay aleatorio entre 1.0 y 2.5 s dentro del hilo (pausa etica).
            time.sleep(random.uniform(1.0, 2.5))
