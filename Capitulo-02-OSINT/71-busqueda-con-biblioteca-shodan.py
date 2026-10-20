# Diapositiva 71: Instalacion y uso de shodan
# Usa la biblioteca oficial de Shodan para buscar servidores por filtros,
# cargando la clave de API desde una variable de entorno (nunca en el codigo).

import os  # modulo para leer variables de entorno del sistema
import shodan  # biblioteca oficial del servicio Shodan

api = shodan.Shodan(os.environ["SHODAN_API_KEY"])  # creamos el cliente con la clave tomada del entorno
try:  # las llamadas a la API pueden fallar por cuota o red
    resultados = api.search("apache country:ES")  # buscamos servidores Apache ubicados en Espana
    print(f"Total de resultados: {resultados['total']}")  # cuantos coincidieron en total
    for host in resultados["matches"][:5]:  # recorremos solo los primeros cinco resultados
        print(f"IP: {host['ip_str']}  Puerto: {host['port']}")  # mostramos IP y puerto de cada host
        print(f"Organizacion: {host.get('org', 'N/D')}")  # mostramos la organizacion, o N/D si falta
        print("---")  # separador visual entre resultados
except shodan.APIError as e:  # capturamos los errores propios de Shodan
    print(f"[-] Error de Shodan: {e}")  # avisamos del fallo sin que el programa se caiga
