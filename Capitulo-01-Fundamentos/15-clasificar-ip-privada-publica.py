# Diapositiva 15: Indentacion, la regla de oro de Python
# Version robusta: clasifica una IP como privada o publica y detecta
# entradas invalidas usando el modulo ipaddress (y mostrando la indentacion).

# Trae el modulo ipaddress, que valida y clasifica direcciones IP.
import ipaddress


# Funcion que recibe el objetivo como texto y devuelve un texto con la clasificacion.
def clasificar(objetivo: str) -> str:
    """Clasifica una IP como privada o publica; detecta entradas invalidas."""
    # "try" intenta ejecutar algo que podria fallar.
    try:
        # Convierte el texto en un objeto IP; si el texto no es una IP valida, lanza un error.
        ip = ipaddress.ip_address(objetivo)
    # "except" atrapa el error ValueError que aparece cuando la IP no es valida.
    except ValueError:
        # "return" termina la funcion devolviendo este texto.
        return "IP invalida"
    # "if" evalua una condicion; .is_private es True si la IP es de red privada.
    if ip.is_private:
        return "El objetivo esta en la red local (privada)"
    # Si no entro al if anterior, llega aqui: la IP es publica.
    return "El objetivo es externo (publica)"


# Recorre varias IP de ejemplo, validas e invalidas.
for o in ["192.168.1.1", "10.0.0.5", "172.20.1.1", "8.8.8.8", "192.168.300.1"]:
    # {o:<15} alinea el texto a la izquierda en 15 espacios y muestra la clasificacion.
    print(f"{o:<15} -> {clasificar(o)}")
