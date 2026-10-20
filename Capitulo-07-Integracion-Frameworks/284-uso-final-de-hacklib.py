# Diapositiva 284: hacklib en produccion, uso e imperativo legal
# Muestra el uso final de la biblioteca ya empaquetada: importar una herramienta,
# instanciarla, ejecutarla y guardar los resultados en pocas lineas.
# (El aviso legal del README se incluye como comentario al final; en el original va en markdown.)

# Uso final de hacklib (Python 3.11)
from hacklib import EscanerPuertos  # importamos la herramienta desde la biblioteca instalada

escaner = EscanerPuertos(config_path="config/settings.yaml")  # creamos la herramienta indicando su configuracion
hallazgos = escaner.ejecutar("scanme.nmap.org")   # ejecutamos el escaneo contra un objetivo autorizado
escaner.guardar_resultado(hallazgos, "resultados/escaneo_01.json")  # guardamos los hallazgos en un archivo JSON

# AVISO LEGAL (va como primera seccion del README.md):
# Esta biblioteca esta disenada exclusivamente para pruebas de penetracion
# autorizadas. El uso sin autorizacion escrita puede constituir un delito
# (en Colombia, Ley 1273 de 2009).
