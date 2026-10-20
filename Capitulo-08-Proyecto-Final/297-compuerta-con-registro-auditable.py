# Diapositiva 297: Gate review, sin entregable no se avanza
# Muestra una compuerta que valida el proyecto y deja un registro auditable
# con fecha, usuario, estado y una huella (hash) del proyecto.

# getpass permite saber el nombre del usuario del sistema.
import getpass
# hashlib calcula huellas digitales como SHA-256.
import hashlib
# json convierte diccionarios en texto y viceversa.
import json
# logging escribe mensajes en un archivo de registro.
import logging
# datetime y timezone permiten trabajar con fechas y con la hora universal (UTC).
from datetime import datetime, timezone

# Configuramos el log: se guarda en auditoria.log, con nivel informativo y solo el mensaje.
logging.basicConfig(filename="auditoria.log", level=logging.INFO,
                    format="%(message)s")

# Diccionario con el proyecto que vamos a validar.
proyecto = {"nombre_cliente": "Lab", "autorizacion_firmada": True}
# Calculamos la huella SHA-256 del proyecto en texto ordenado y tomamos los primeros 16 caracteres.
huella = hashlib.sha256(json.dumps(proyecto, sort_keys=True).encode()).hexdigest()[:16]
# Buscamos campos vacios recorriendo las parejas clave-valor del diccionario.
faltantes = [c for c, v in proyecto.items() if not v]
# Si no falta nada queda APROBADO; si falta algo, RECHAZADO.
estado = "APROBADO" if not faltantes else "RECHAZADO"

# Armamos la linea de registro con fecha UTC, usuario, nombre de la compuerta, estado y huella.
linea = (f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} | "
         f"usuario={getpass.getuser()} | gate=alcance | estado={estado} | sha256={huella}")
# Escribimos la linea en el archivo de auditoria.
logging.info(linea)
# Tambien la mostramos en pantalla.
print(linea)
