# Diapositiva 293: Formulario de kickoff y documento de alcance
# Muestra como decidir si un activo (una IP o un dominio) esta dentro del
# alcance autorizado, usando notacion CIDR para redes y comodines para dominios.

# fnmatch compara textos contra patrones con comodines, por ejemplo *.cliente.lab.
import fnmatch
# ipaddress entiende de direcciones IP y de redes (rangos) en notacion CIDR.
import ipaddress

# Diccionario con las tres listas del alcance: redes permitidas, dominios permitidos y exclusiones.
ALCANCE = {
    "redes": ["192.168.56.0/24"],
    "dominios": ["*.cliente.lab", "cliente.lab"],
    "fuera": ["192.168.56.1"],          # puerta de enlace: fuera aunque este en la red
}


# Definimos una funcion que recibe un activo (texto) y devuelve True o False.
def en_alcance(activo: str) -> bool:
    # Si el activo esta en la lista de exclusiones, se rechaza de inmediato.
    if activo in ALCANCE["fuera"]:
        return False                    # lo excluido gana siempre
    # Intentamos interpretar el activo como una direccion IP.
    try:
        ip = ipaddress.ip_address(activo)
        # any devuelve True si la IP pertenece a alguna de las redes permitidas.
        return any(ip in ipaddress.ip_network(r) for r in ALCANCE["redes"])
    # Si el texto no es una IP valida, Python lanza ValueError y lo tratamos como dominio.
    except ValueError:                  # no es IP: se trata como dominio
        # Comprobamos si el dominio coincide con alguno de los patrones permitidos.
        return any(fnmatch.fnmatch(activo, p) for p in ALCANCE["dominios"])


# Recorremos varios activos de prueba para ver si quedan dentro o fuera.
for a in ("192.168.56.101", "192.168.56.1", "10.0.0.5", "www.cliente.lab", "cliente.com"):
    # :<16 alinea el texto a la izquierda en 16 espacios para que la tabla quede ordenada.
    print(f"{a:<16} {'DENTRO' if en_alcance(a) else 'FUERA'}")
