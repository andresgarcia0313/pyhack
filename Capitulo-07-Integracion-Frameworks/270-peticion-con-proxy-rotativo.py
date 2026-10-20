# Diapositiva 270: Rotacion con lista de proxys externos, parte 2
# Muestra una funcion que hace una peticion usando un proxy aleatorio de la lista
# e informa cual proxy se uso, para poder depurar los que fallan.
# (Fragmento: usa obtener_proxy_aleatorio y requests de la diapositiva 269.)

def peticion_con_proxy_rotativo(url: str):  # funcion que hace un GET a la url con un proxy al azar
    """Realiza una peticion usando un proxy aleatorio de la lista."""  # texto de ayuda de la funcion
    proxies = obtener_proxy_aleatorio()  # pedimos un proxy aleatorio en formato de diccionario
    try:  # intentamos la peticion y capturamos errores
        respuesta = requests.get(url, proxies=proxies, timeout=30)  # hacemos el GET a traves de ese proxy
        print(f"[+] {url} via {proxies['http']} -> {respuesta.status_code}")  # mostramos url, proxy y codigo de estado
        return respuesta  # devolvemos la respuesta para usarla fuera
    except requests.exceptions.RequestException as e:  # si la peticion falla
        print(f"[-] Error con proxy {proxies['http']}: {e}")  # reportamos el error indicando que proxy fallo
        return None  # devolvemos None para avisar que no hubo respuesta
