# Diapositiva 23: Excepciones relevantes en herramientas de red
# Muestra como cada excepcion de red da un diagnostico distinto y por que el
# orden de los except importa (del mas especifico al mas general).

# Trae socket para las conexiones y errores de red.
import socket


# Recibe host y puerto, devuelve un texto con el diagnostico.
def diagnosticar(host: str, puerto: int) -> str:
    # Intenta conectar con un segundo de espera.
    try:
        with socket.create_connection((host, puerto), timeout=1):
            return "abierto"
    # El nombre no se pudo resolver a una IP.
    except socket.gaierror:
        return "nombre no resuelve"
    # El host respondio pero el puerto esta cerrado (paquete RST).
    except ConnectionRefusedError:
        return "cerrado (respondio RST)"
    # No hubo respuesta a tiempo; es el mismo objeto que socket.timeout desde Python 3.10.
    except TimeoutError:                     # mismo objeto que socket.timeout
        return "filtrado o host caido (sin respuesta)"
    # Red de seguridad: cualquier otro error de red; va al final por ser el mas general.
    except OSError as e:                     # red de seguridad, va al final
        return f"otro error de red: {e}"


# "is" comprueba que son el mismo objeto; desde 3.10 socket.timeout es TimeoutError.
print(socket.timeout is TimeoutError)
# Prueba contra localhost en un puerto cerrado.
print(diagnosticar("127.0.0.1", 9))
# Prueba contra un nombre que no existe.
print(diagnosticar("no-existe.invalid", 80))
