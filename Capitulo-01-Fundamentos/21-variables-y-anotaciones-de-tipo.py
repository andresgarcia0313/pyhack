# Diapositiva 21: Variables con anotaciones de tipo
# Muestra que las anotaciones de tipo son solo documentacion: Python no las
# verifica al ejecutar (quien si lo hace es mypy).

# Trae sys para poder leer las anotaciones del propio modulo.
import sys
# Variable de texto con la IP objetivo.
target_ip: str = "192.168.56.101"
# Lista de enteros, aun vacia, para los puertos abiertos.
open_ports: list[int] = []
# Bandera booleana que empieza en False.
is_reachable: bool = False
# Diccionario que asocia un host (texto) con una lista de puertos (enteros).
scan_results: dict[str, list[int]] = {}

# Anotamos "int" pero asignamos texto; Python NO se queja al ejecutar.
puerto: int = "veintidos"          # Python no se queja al ejecutar
# type(puerto).__name__ revela que en realidad es str (texto).
print(type(puerto).__name__)        # str
# __annotations__ guarda las anotaciones; aqui se ve que quedo registrada como int.
print(sys.modules[__name__].__annotations__["puerto"])  # solo queda registrada

# .append(22) agrega el numero 22 al final de la lista.
open_ports.append(22)
# Asigna esa lista como valor de la clave target_ip en el diccionario.
scan_results[target_ip] = open_ports
# Muestra el diccionario final.
print(scan_results)
