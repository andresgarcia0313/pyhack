# Diapositiva 18: 1.2 Variables, funciones y manejo de errores
# Muestra la diferencia entre callar un error (caida silenciosa) y reportarlo,
# al resolver un nombre que no existe.

# Trae el modulo socket para resolver nombres a IP.
import socket


# Version "mal": recibe host (texto) y devuelve texto.
def mal(host: str) -> str:
    # Intenta resolver el nombre.
    try:
        return socket.gethostbyname(host)
    # Atrapa cualquier error y lo ignora.
    except Exception:
        return ""                 # caida silenciosa: nadie se entera


# Version "bien": devuelve texto o None (str | None significa "texto o nada").
def bien(host: str) -> str | None:
    # Intenta resolver el nombre.
    try:
        return socket.gethostbyname(host)
    # Atrapa solo el error de resolucion y guarda el objeto del error en "e".
    except socket.gaierror as e:
        # Informa el problema; {host!r} muestra el valor con comillas y e.strerror es el mensaje del sistema.
        print(f"[ERROR] No resolvio {host!r}: {e.strerror}")
        return None               # el llamador sabe que no hay dato


# repr(...) muestra el valor tal cual, con comillas; aqui la cadena vacia.
print(repr(mal("no-existe.invalid")))
# Aqui se ve el mensaje de error y luego None.
print(repr(bien("no-existe.invalid")))
