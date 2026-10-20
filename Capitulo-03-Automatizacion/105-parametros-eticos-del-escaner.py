# Diapositiva 105: Escaner de subdominios, diseno de la herramienta
# Muestra las constantes eticas del escaner: concurrencia, delays, limite
# de reintentos y timeout. USO EXCLUSIVO en entornos autorizados.

# Parametros eticos del escaner (constantes configurables).

# Numero maximo de peticiones simultaneas.
MAX_HILOS = 3
# Segundos minimos de pausa entre peticiones.
DELAY_MIN = 0.8
# Segundos maximos de pausa entre peticiones.
DELAY_MAX = 2.0
# Cuantas veces reintentar ante errores temporales.
MAX_REINTENTOS = 3
# Segundos de espera maxima por respuesta.
TIMEOUT = 6

# USO EXCLUSIVO: dominios propios, lab del curso o scanme.nmap.org.
