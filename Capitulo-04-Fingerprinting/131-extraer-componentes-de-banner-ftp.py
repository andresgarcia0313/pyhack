# Diapositiva 131: Ejemplos de informacion revelada
# Muestra como, a partir de un banner FTP ya capturado, se separan sus componentes
# (codigo, software y version) con un parseo simple por espacios.

# A partir de un banner FTP capturado, extraer sus componentes
banner_ftp = "220 ProFTPD 1.3.5 Server (Debian) [::ffff:192.168.1.10]"  # texto de ejemplo de un banner FTP

# Un parseo simple separando por espacios y parentesis
partes = banner_ftp.split()  # divide el texto en una lista usando los espacios como separador
codigo = partes[0]            # '220' -> servicio listo  (primer elemento de la lista)
software = partes[1]          # 'ProFTPD'  (segundo elemento)
version = partes[2]           # '1.3.5'  (tercer elemento)
print(f"Codigo: {codigo} | Software: {software} | Version: {version}")  # arma e imprime un resumen legible
# Salida: Codigo: 220 | Software: ProFTPD | Version: 1.3.5
