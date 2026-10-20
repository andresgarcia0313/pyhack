# Diapositiva 114: Funcion normalize_record, timestamp e IP (parte 2)
# Muestra como se normaliza la IP: se aceptan alias y se valida con el
# modulo ipaddress; si es invalida o falta, el campo queda en None.

# "ipaddress" valida y estandariza direcciones IPv4 e IPv6.
import ipaddress

# Suponemos un record en construccion (ver diapositiva 113).
record = {}
# Diccionario crudo de ejemplo que llega de una fuente.
raw = {"ip": "8.8.8.8 "}

# Aceptamos varios nombres para la IP; si ninguno viene, usamos cadena vacia.
ip_raw = raw.get("ip") or raw.get("ip_address") or raw.get("host") or ""
# "try" protege la validacion, que falla si el texto no es una IP.
try:
    # Validamos y estandarizamos; ".strip()" quita espacios accidentales.
    record["ip_address"] = str(ipaddress.ip_address(ip_raw.strip()))
# Si no era una IP valida, dejamos el campo en None (honesto, no basura).
except ValueError:
    record["ip_address"] = None

# Ejemplos:
# "8.8.8.8 "   -> "8.8.8.8"
# "no-ip"      -> None
