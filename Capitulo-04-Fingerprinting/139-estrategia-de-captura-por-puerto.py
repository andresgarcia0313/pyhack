# Diapositiva 139: Puertos y protocolos relevantes para banner grabbing
# Muestra un diccionario que indica que estrategia de captura usar en cada puerto
# (leer directo, enviar HEAD, negociar TLS o leer un handshake binario).

# Diccionario operativo: que estrategia usar por puerto
ESTRATEGIA = {  # la clave es el numero de puerto y el valor es la accion recomendada
    21:  "leer directo",          22:  "leer directo",            # FTP y SSH saludan solos
    25:  "leer directo",          110: "leer directo",            # SMTP y POP3 saludan solos
    143: "leer directo",          3306: "leer handshake binario", # IMAP directo; MySQL manda bytes binarios
    80:  "enviar HEAD y leer",    443: "negociar TLS, luego HEAD",# HTTP necesita peticion; HTTPS ademas TLS
}
for puerto, accion in sorted(ESTRATEGIA.items()):  # recorre los puertos ordenados de menor a mayor
    print(f"Puerto {puerto:>4}: {accion}")  # imprime el puerto alineado a la derecha y su accion
