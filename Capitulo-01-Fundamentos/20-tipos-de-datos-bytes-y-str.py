# Diapositiva 20: Tipos de datos clave en herramientas de seguridad
# Muestra los tipos str, bytes, int, bool y dict, y como un banner pasa de
# bytes (lo que viaja por la red) a texto de forma segura.

# bytes: secuencia de numeros crudos; la "b" marca bytes y \r\n, \xff son caracteres especiales.
banner_crudo: bytes = b"SSH-2.0-OpenSSH_8.2p1 Ubuntu\r\n\xff"
# .decode convierte bytes a texto; errors="replace" evita fallar con bytes invalidos; .strip() limpia los bordes.
banner: str = banner_crudo.decode("utf-8", errors="replace").strip()
# int: numero entero, usado para puertos.
puerto: int = 22
# bool: valor logico, True o False.
abierto: bool = True
# dict: diccionario que asocia clave de texto con valor de texto.
cabeceras: dict[str, str] = {"User-Agent": "curso-pyt-hack/1.0"}

# type(...).__name__ da el nombre del tipo; muestra que paso de bytes a str.
print(type(banner_crudo).__name__, "->", type(banner).__name__)
# {banner!r} muestra el texto con comillas para ver los caracteres especiales.
print(f"[+] {puerto}/tcp abierto={abierto} banner={banner!r}")
# .encode() convierte texto a bytes: eso es lo que realmente se envia por un socket.
print("HEAD / HTTP/1.0\r\n\r\n".encode())   # lo que realmente se envia
