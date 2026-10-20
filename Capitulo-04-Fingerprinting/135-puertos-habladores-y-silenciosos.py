# Diapositiva 135: Tecnicas de extraccion de banners y cabeceras (introduccion)
# Muestra la diferencia entre puertos "habladores" (saludan solos, como FTP)
# y "silenciosos" (hay que estimularlos, como HTTP en el puerto 80).

# Dos comportamientos distintos segun el protocolo
# FTP (habla solo): conectar y leer basta
# HTTP (callado): hay que enviar una peticion primero
import socket  # se importa aunque este ejemplo solo clasifica puertos (patron del libro)


def es_hablador(puerto: int) -> bool:  # funcion que responde Si/No (True/False) a "este puerto saluda solo?"
    """Puertos que suelen enviar banner sin estimulo."""  # texto de ayuda de la funcion
    return puerto in (21, 22, 25, 110, 143)  # True si el puerto esta en esa lista de puertos habladores


for p in (21, 80):  # recorre dos puertos de ejemplo: 21 (FTP) y 80 (HTTP)
    print(f"Puerto {p}: {'saluda solo' if es_hablador(p) else 'hay que estimularlo'}")  # imprime el texto segun el caso
# Puerto 21: saluda solo
# Puerto 80: hay que estimularlo
