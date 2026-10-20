# Diapositiva 32: Patron combinado, mini escaner de puertos
# Muestra el patron capturar, deduplicar, enriquecer y reportar usando las
# cuatro estructuras: lista, set, diccionario y comprension.

# 1. Lista: define los puertos objetivo en orden.
PUERTOS_OBJETIVO = [22, 80, 443, 8080]                    # 1. lista: orden
# Resultados crudos de dos pasadas, con duplicados.
crudos = [80, 22, 80, 443, 22]                            #    resultados de dos pasadas
# 2. set: elimina los puertos repetidos.
unicos = set(crudos)                                      # 2. set: deduplicar
# 3. diccionario: asocia cada puerto con el nombre de su servicio.
SERVICIOS = {22: "SSH", 80: "HTTP", 443: "HTTPS"}         # 3. dict: enriquecer
# 4. comprension de lista: arma el reporte; .get(p, '?') pone '?' si no conoce el servicio; sorted ordena.
reporte = [f"{p}/tcp {SERVICIOS.get(p, '?')}" for p in sorted(unicos)]  # 4. comprension
# Muestra el reporte final.
print(reporte)
# set(PUERTOS_OBJETIVO) - unicos da los puertos objetivo que no respondieron.
print(f"No respondieron: {sorted(set(PUERTOS_OBJETIVO) - unicos)}")
