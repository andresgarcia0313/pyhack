# Diapositiva 54: Consulta a crt.sh, parte 2
# Demuestra el diseno a prueba de fallos: si una fuente falla, la funcion
# devuelve una lista vacia y el flujo continua con las demas fuentes OSINT.

import requests  # biblioteca para peticiones HTTP


def obtener_subdominios_crtsh(dominio: str) -> list[str]:  # misma funcion de la diapositiva 53
    """Consulta crt.sh y devuelve subdominios unicos. No contacta al objetivo."""  # descripcion
    url = f"https://crt.sh/?q=%.{dominio}&output=json"  # URL con el comodin % y salida JSON
    try:  # protegemos la consulta de red
        respuesta = requests.get(url, timeout=10)  # pedimos los datos con limite de 10 segundos
        respuesta.raise_for_status()  # un codigo de error HTTP se vuelve excepcion
        subdominios = set()  # conjunto que descarta repetidos
        for entrada in respuesta.json():  # recorremos el arreglo JSON
            for sub in entrada.get("name_value", "").split("\n"):  # separamos nombres por salto de linea
                subdominios.add(sub.strip())  # guardamos cada nombre limpio
        return sorted(subdominios)  # devolvemos la lista ordenada
    except requests.RequestException as e:  # capturamos fallos de red o HTTP
        print(f"[-] Error al consultar crt.sh: {e}")  # avisamos del fallo
        return []  # devolvemos lista vacia en vez de caernos


# Comportamiento a prueba de fallos: aunque la fuente falle, el flujo sigue.
resultado = obtener_subdominios_crtsh("dominio-inexistente.invalid")  # dominio que fallara a proposito
print(f"Subdominios encontrados: {len(resultado)}")  # imprime 0 porque la lista vino vacia, sin caerse
print("[*] Continuo con las demas fuentes OSINT...")  # el programa continua pese al error anterior
