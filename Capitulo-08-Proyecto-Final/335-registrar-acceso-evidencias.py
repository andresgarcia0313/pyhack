# Diapositiva 335: Gestion segura de claves y acceso a evidencias
# Muestra como dejar una cadena de custodia minima: registrar quien accedio a
# cada evidencia, cuando y que accion hizo, en un archivo de registro.

# getpass obtiene el nombre del usuario del sistema.
import getpass
# datetime y timezone dan la fecha y hora en UTC.
from datetime import datetime, timezone


# Funcion que agrega una linea al registro de custodia y la devuelve.
def registrar_acceso(evidencia: str, accion: str) -> str:
    # Armamos la linea con fecha UTC, usuario, nombre de la evidencia y accion.
    linea = (f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} | "
             f"usuario={getpass.getuser()} | evidencia={evidencia} | accion={accion}")
    # Abrimos el archivo en modo "a" (agregar al final) para no borrar lo anterior.
    with open("custodia.log", "a", encoding="utf-8") as f:
        # Escribimos la linea y un salto de linea.
        f.write(linea + "\n")
    # Devolvemos la linea registrada.
    return linea


# Registramos un acceso de lectura a una evidencia cifrada y mostramos la linea.
print(registrar_acceso("FIND-001_captura.png.enc", "lectura"))
