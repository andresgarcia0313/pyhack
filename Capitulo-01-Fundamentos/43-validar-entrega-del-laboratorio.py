# Diapositiva 43: Resultados esperados
# Script de verificacion del entregable del laboratorio: abre el JSON generado,
# comprueba sus claves y muestra datos clave. Ejecutar desde toolkit/.

# json lee el archivo JSON; Path maneja la ruta.
import json
from pathlib import Path

# Ruta del JSON que produjo el recolector del laboratorio.
ruta = Path("data/recoleccion_sistema.json")
# read_text lee el archivo y json.loads lo convierte en estructura de Python.
datos = json.loads(ruta.read_text(encoding="utf-8"))
# Conjunto con las claves que deben existir en el JSON.
esperadas = {"metadata", "sistema", "red", "puertos", "entorno", "interfaces"}
# ruta.stat().st_size da el tamano del archivo en bytes.
print(f"[+] Tamano: {ruta.stat().st_size} bytes")
# "<=" entre conjuntos pregunta si todas las esperadas estan dentro de las claves del JSON.
print(f"[+] Claves completas: {esperadas <= datos.keys()}")
# Accede a la lista de puertos abiertos dentro de la clave "puertos".
print(f"[+] Puertos abiertos: {datos['puertos']['abiertos']}")
# Muestra el identificador del laboratorio y la marca de tiempo guardada.
print(f"[+] Lab: {datos['metadata']['lab']} | {datos['metadata']['timestamp']}")
