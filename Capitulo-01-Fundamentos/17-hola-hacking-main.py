# Diapositiva 17: Secuencia general de trabajo
# Script hola_hacking.py: valida que el entorno del curso funciona (version,
# venv y red local) y muestra el patron if __name__ == "__main__".

"""Valida que el entorno del curso funciona: version, venv y red local."""
# Trae socket (red) y sys (informacion del interprete).
import socket
import sys


# Devuelve un diccionario cuyas claves y valores son texto (dict[str, str]).
def info_entorno() -> dict[str, str]:
    """Reune datos basicos del entorno de trabajo."""
    # Construye y devuelve el diccionario con los datos recogidos.
    return {
        # Numero de version de Python.
        "python": sys.version.split()[0],
        # "si" si hay venv activo, "no" si no; compara las dos rutas del interprete.
        "venv": "si" if sys.prefix != sys.base_prefix else "no",
        # Nombre del equipo.
        "hostname": socket.gethostname(),
        # IP a la que resuelve localhost.
        "localhost": socket.gethostbyname("localhost"),
    }


# Funcion principal; no devuelve nada util.
def main() -> None:
    # .items() recorre el diccionario entregando clave y valor en cada vuelta.
    for clave, valor in info_entorno().items():
        # {clave:<10} alinea la clave a la izquierda en 10 espacios.
        print(f"[+] {clave:<10}: {valor}")


# __name__ vale "__main__" solo si el archivo se ejecuta directo; asi main() no corre al importarlo.
if __name__ == "__main__":  # solo corre si se ejecuta directamente
    main()
