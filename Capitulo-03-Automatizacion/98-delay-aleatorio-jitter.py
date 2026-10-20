# Diapositiva 98: Semaforos, parte 2
# Muestra la diferencia entre un delay fijo y uno aleatorio (jitter): el
# azar rompe la regularidad y hace el patron mas discreto.

# "random" genera el numero al azar; "time" permitiria aplicar la pausa real.
import random, time

# Comparacion: delay fijo contra jitter, en tres repeticiones.
for _ in range(3):
    # Delay fijo: siempre el mismo valor, facil de detectar como automatico.
    fijo = 1.0
    # Jitter: numero decimal al azar entre 1.0 y 2.5 que rompe la regularidad.
    variable = random.uniform(1.0, 2.5)
    # Mostramos ambos; ":.2f" recorta el decimal a dos cifras.
    print(f"fijo={fijo}  variable={variable:.2f}")

# Salida ejemplo:
# fijo=1.0  variable=1.87
# fijo=1.0  variable=2.31
# fijo=1.0  variable=1.12
