# Diapositiva 154: Flujo completo - de conexion a reporte
# Muestra la regla de decision de la leccion: que herramienta usar segun el puerto
# (requests para HTTP/HTTPS, socket para servicios de texto plano).

# Regla de decision resumida de la leccion
def herramienta_para(puerto: int) -> str:  # recibe un puerto y recomienda la herramienta
    if puerto in (80, 443, 8080, 8443):  # si es un puerto web
        return "requests (HTTP/HTTPS, maneja TLS y redirecciones)"  # usamos requests
    return "socket (texto plano: FTP, SSH, SMTP, POP3, IMAP)"  # para el resto, socket


for p in (21, 22, 80, 443):  # recorre cuatro puertos de ejemplo
    print(f"Puerto {p:>3}: {herramienta_para(p)}")  # imprime el puerto y la herramienta recomendada
# El resultado de ambas vias se consolida en un unico JSON con timestamps
