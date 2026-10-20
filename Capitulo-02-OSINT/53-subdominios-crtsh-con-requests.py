# Diapositiva 53: Consulta a crt.sh para descubrir subdominios
# Consulta el registro publico de transparencia de certificados (crt.sh) para
# enumerar subdominios unicos de un dominio, sin contactar al objetivo.

import requests  # biblioteca para hacer peticiones HTTP de forma sencilla


def obtener_subdominios_crtsh(dominio: str) -> list[str]:  # recibe el dominio y devuelve una lista de textos
    """Consulta crt.sh y devuelve subdominios unicos. No contacta al objetivo."""  # descripcion de la funcion
    url = f"https://crt.sh/?q=%.{dominio}&output=json"  # armamos la URL con el comodin % y formato JSON
    try:  # protegemos la consulta de red ante fallos
        respuesta = requests.get(url, timeout=10)  # pedimos los datos, con 10 segundos de limite
        respuesta.raise_for_status()  # lanza una excepcion si el codigo HTTP es de error (4xx o 5xx)
        subdominios = set()  # un conjunto no admite repetidos: deduplica solo
        for entrada in respuesta.json():  # recorremos cada objeto del arreglo JSON
            for sub in entrada.get("name_value", "").split("\n"):  # un campo puede traer varios nombres por linea
                subdominios.add(sub.strip())  # agregamos cada nombre sin espacios sobrantes
        return sorted(subdominios)  # devolvemos la lista ordenada alfabeticamente
    except requests.RequestException as e:  # capturamos solo fallos de red o de HTTP
        print(f"[-] Error al consultar crt.sh: {e}")  # avisamos del error
        return []  # devolvemos lista vacia para que el flujo pueda continuar


for s in obtener_subdominios_crtsh("scanme.nmap.org"):  # llamamos a la funcion y recorremos el resultado
    print(s)  # imprimimos cada subdominio encontrado
