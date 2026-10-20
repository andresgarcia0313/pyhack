# Diapositiva 41: Resumen del capitulo
# Resumen ejecutable que combina lista, conjunto, diccionario, funcion tipada
# y excepciones especificas en pocas lineas, contra localhost.

# Trae socket para las conexiones.
import socket

# Lista de puertos con un duplicado (el 22 aparece dos veces).
PUERTOS: list[int] = [22, 80, 22, 443]                     # lista con duplicados
# Diccionario que asocia puerto con el nombre de su servicio.
SERVICIOS: dict[int, str] = {22: "SSH", 80: "HTTP", 443: "HTTPS"}


# Funcion tipada: recibe un puerto y, opcionalmente, un host; devuelve el estado como texto.
def estado(puerto: int, host: str = "127.0.0.1") -> str:   # funcion tipada
    # Intenta conectar con medio segundo de espera.
    try:
        with socket.create_connection((host, puerto), timeout=0.5):
            return "abierto"
    # Excepcion especifica: el puerto respondio cerrado.
    except ConnectionRefusedError:                          # excepcion especifica
        return "cerrado"
    # Excepcion especifica: no hubo respuesta a tiempo.
    except TimeoutError:
        return "filtrado"


# set(PUERTOS) deduplica, sorted ordena, y la comprension asocia cada puerto con (servicio, estado).
print({p: (SERVICIOS.get(p, "?"), estado(p)) for p in sorted(set(PUERTOS))})
