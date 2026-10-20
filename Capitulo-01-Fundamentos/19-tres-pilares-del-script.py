# Diapositiva 19: Los tres pilares de un script de hacking etico
# Muestra en pocas lineas los tres pilares: variable tipada, funcion
# reutilizable y excepcion controlada, probando puertos en localhost.

# Trae socket para las conexiones de red.
import socket

# Pilar 1: variable con tipo anotado; OBJETIVO es texto (str) y guarda la IP.
OBJETIVO: str = "127.0.0.1"                 # pilar 1: variable tipada
# Lista de enteros con los puertos a probar.
PUERTOS: list[int] = [22, 80, 9]


# Pilar 2: funcion que encapsula la logica de probar un puerto; devuelve True o False.
def puerto_abierto(host: str, puerto: int) -> bool:   # pilar 2: funcion
    # Intenta conectar con tiempo de espera de medio segundo.
    try:
        with socket.create_connection((host, puerto), timeout=0.5):
            return True
    # Pilar 3: atrapa el error de red para que no detenga el programa.
    except OSError:                          # pilar 3: excepcion controlada
        return False


# Comprension de diccionario: {p: resultado for p in PUERTOS} prueba cada puerto y arma el diccionario.
print({p: puerto_abierto(OBJETIVO, p) for p in PUERTOS})
