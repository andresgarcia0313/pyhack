# Diapositiva 157: Formas de resultado de fingerprinting (tabla)
# Muestra como inspeccionar el certificado TLS de un objetivo autorizado para leer
# el dominio (CN), los dominios alternativos (SAN) y la fecha de caducidad.

# Inspeccionar el certificado TLS de un objetivo autorizado
import ssl, socket  # ssl maneja el cifrado TLS; socket abre la conexion


def datos_certificado(host: str, puerto: int = 443) -> dict:  # devuelve un diccionario con datos del certificado
    ctx = ssl.create_default_context()  # crea un contexto TLS con la configuracion segura por defecto
    with socket.create_connection((host, puerto), timeout=5) as sock:  # abre la conexion y la cierra sola al terminar
        with ctx.wrap_socket(sock, server_hostname=host) as ssock:  # envuelve el socket con TLS (negocia el cifrado)
            cert = ssock.getpeercert()  # obtiene el certificado que presenta el servidor
    # CN y SAN revelan dominios; 'notAfter' revela la caducidad
    return {"subject": cert.get("subject"), "SAN": cert.get("subjectAltName"),  # datos del titular y dominios cubiertos
            "caduca": cert.get("notAfter")}  # fecha en que el certificado deja de ser valido


print(datos_certificado("scanme.nmap.org") if False else "Ejecutar solo en objetivo autorizado")  # el if False evita ejecutarlo por accidente
