# Diapositiva 163: Taxonomia de servicios por puerto (tabla)
# Muestra como clasificar un servicio por su numero de puerto usando un diccionario,
# y marca el caso de Telnet (23) por transmitir en texto plano.

# Clasificar por tipo usando la taxonomia de la diapositiva
TAXONOMIA = {  # diccionario: numero de puerto -> categoria de servicio
    22: "Acceso remoto", 23: "Acceso remoto", 3389: "Acceso remoto",  # SSH, Telnet, RDP
    21: "Transferencia", 445: "Transferencia",  # FTP, SMB
    80: "Servicio web", 443: "Servicio web",  # HTTP, HTTPS
    3306: "Base de datos", 5432: "Base de datos", 1433: "Base de datos",  # MySQL, PostgreSQL, MSSQL
    25: "Correo", 389: "Directorio",  # SMTP, LDAP
}
for puerto in (23, 3306, 443):  # recorre tres puertos de ejemplo
    tipo = TAXONOMIA.get(puerto, "Desconocido")  # busca la categoria; si no esta, "Desconocido"
    alerta = " <- texto plano, obsoleto" if puerto == 23 else ""  # aviso especial para Telnet (puerto 23)
    print(f"Puerto {puerto:>4}: {tipo}{alerta}")  # imprime el puerto, su tipo y la posible alerta
