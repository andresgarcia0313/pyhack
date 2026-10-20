# Diapositiva 94: Concurrencia controlada y delay etico
# Muestra las dos palancas que definen la tasa de peticiones: cuantas van
# en paralelo (hilos) y cuanto se espera entre ellas (delay).

# Palanca 1: numero maximo de peticiones simultaneas.
MAX_HILOS = 3
# Palanca 2: segundos de pausa entre peticiones de un mismo hilo.
DELAY = 1.5

# Con 3 hilos y ~1 s de respuesta mas 1.5 s de pausa:
# aprox. 3 peticiones cada 2.5 s, es decir, cerca de 1.2 req/s, una tasa cortes.
