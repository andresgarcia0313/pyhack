# Diapositiva 254: Conexion RPC y busqueda de modulos SMB, parte 2
# Muestra como imprimir solo una muestra de 5 modulos para identificar
# rapidamente el que necesitamos, sin saturar la pantalla.
# (Fragmento: continua el codigo de la diapositiva 253, donde se creo "modulos_auxiliares".)

for mod in modulos_auxiliares[:5]:  # recorremos solo los primeros 5 elementos de la lista
    print(f"    - {mod['fullname']}")  # imprimimos el nombre completo de cada modulo
