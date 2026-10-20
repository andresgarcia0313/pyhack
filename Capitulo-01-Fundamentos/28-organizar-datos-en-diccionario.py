# Diapositiva 28: 1.3 Estructuras de datos aplicadas a herramientas
# Muestra el mismo dato mal organizado (textos para partir) y bien organizado
# (diccionario anidado), con consulta directa.

# Lista de textos crudos con el formato "ip:puerto:estado".
crudo = ["192.168.56.101:22:abierto", "192.168.56.101:80:cerrado", "192.168.56.102:22:abierto"]

# Diccionario que asociara cada IP con otro diccionario de puerto -> estado.
estructurado: dict[str, dict[int, str]] = {}
# Recorre cada linea cruda.
for linea in crudo:
    # .split(":") parte el texto en tres partes y las asigna a tres variables.
    ip, puerto, estado = linea.split(":")
    # setdefault(ip, {}) devuelve el diccionario del host (o lo crea vacio); luego guarda el estado con el puerto como clave entera.
    estructurado.setdefault(ip, {})[int(puerto)] = estado

# Muestra la estructura completa ya organizada.
print(estructurado)
# Consulta directa: estado del puerto 22 de esa IP, sin partir textos.
print(estructurado["192.168.56.101"][22])      # consulta directa, sin partir textos
