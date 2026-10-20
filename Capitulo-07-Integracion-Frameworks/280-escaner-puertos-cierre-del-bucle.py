# Diapositiva 280: EscanerPuertos, parte 2 y configuracion YAML
# Muestra el cierre del bucle de escaneo: si connect_ex devuelve 0, el puerto
# esta abierto, se agrega a los hallazgos y se registra en el log.
# (Fragmento: va dentro del bucle de la diapositiva 279. La configuracion YAML
#  que lo acompana se incluye como comentario al final, no es codigo Python.)

# tools/escaner_puertos.py  (cierre del bucle)
if s.connect_ex((objetivo, puerto)) == 0:  # connect_ex devuelve 0 cuando el puerto esta abierto
    hallazgos["puertos_abiertos"].append(puerto)  # agregamos el puerto a la lista de abiertos
    self.logger.info("Puerto abierto: %d en %s", puerto, objetivo)  # registramos el hallazgo en el log

# config/settings.yaml (extracto de la misma diapositiva, para referencia):
# general:
#   timeout: 2.0
#   max_hilos: 10
# escaneo:
#   puertos_comunes: [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
# osint:
#   shodan_api_key: "${SHODAN_API_KEY}"   # se lee de variable de entorno
