# Diapositiva 33: Mini escaner, codigo completo del patron combinado
# Muestra una configuracion con nombres (NamedTuple) que no pierde la
# inmutabilidad, y una comprension de diccionario que enriquece puertos.

# ipaddress maneja redes IP; NamedTuple crea tuplas con campos nombrados.
import ipaddress
from typing import NamedTuple


# Define una tupla con nombres: cada campo tiene su tipo.
class ConfigEscaneo(NamedTuple):
    red: str
    timeout_ms: int
    max_hilos: int


# Crea la configuracion; se puede pasar por posicion o por nombre.
CONFIG = ConfigEscaneo("192.168.56.0/30", timeout_ms=100, max_hilos=1000)
# Acceso por nombre (.timeout_ms) o por posicion ([2]); ambos funcionan.
print(CONFIG.timeout_ms, CONFIG[2])                    # por nombre o por posicion
# ip_network(...).hosts() da las IP utilizables de la red; la comprension las vuelve texto.
print([str(ip) for ip in ipaddress.ip_network(CONFIG.red).hosts()])

# Diccionario que asocia puerto con el nombre de su servicio.
servicios_conocidos = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP",
                       443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"}
# set(...) deduplica la lista de puertos abiertos.
puertos_abiertos = set([80, 443, 22, 80, 443])
# Comprension de diccionario: para cada puerto, su servicio o "Desconocido".
reporte = {p: servicios_conocidos.get(p, "Desconocido") for p in puertos_abiertos}
# dict(sorted(...)) ordena los pares por clave antes de mostrarlos.
print(dict(sorted(reporte.items())))
