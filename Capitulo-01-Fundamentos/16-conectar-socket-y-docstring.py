# Diapositiva 16: Comentarios y docstrings en codigo de seguridad
# Muestra una funcion documentada con docstring que intenta una conexion TCP
# a localhost y devuelve True o False.

# Trae el modulo socket, que permite abrir conexiones de red.
import socket


# host: str y puerto: int son los datos de entrada; timeout tiene valor por defecto 1.0; devuelve bool.
def conectar(host: str, puerto: int, timeout: float = 1.0) -> bool:
    """
    Intenta una conexion TCP al host y puerto indicados.

    Args:
        host: nombre o IP autorizada (en el curso, localhost o la VM).
        puerto: numero de puerto TCP (1 a 65535).
        timeout: segundos maximos de espera.

    Returns:
        True si la conexion fue exitosa, False en caso contrario.
    """
    # Intenta la operacion de red, que puede fallar.
    try:
        # "with" abre la conexion y la cierra sola al terminar; create_connection intenta conectar.
        with socket.create_connection((host, puerto), timeout=timeout):
            # Si conecto, devuelve True.
            return True
    # OSError cubre rechazo, tiempo agotado y nombre no resuelto.
    except OSError:  # incluye rechazo, tiempo agotado y nombre no resuelto
        # Si fallo, devuelve False.
        return False


# Prueba la conexion al puerto 9 (discard), casi siempre cerrado.
print(conectar("127.0.0.1", 9))   # puerto discard, casi siempre cerrado
# __doc__ guarda el docstring; .splitlines()[1] toma su segunda linea y .strip() quita espacios de los bordes.
print(conectar.__doc__.splitlines()[1].strip())
