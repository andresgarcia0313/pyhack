# Diapositiva 268: Rotacion automatica, ejecutar_con_rotacion()
# Muestra una rutina que recorre una lista de URL y, cada N peticiones, rota
# la identidad TOR y reporta la nueva IP de salida.
# (Fragmento: usa rotar_identidad_tor, obtener_ip_actual y TOR_PROXY de las diapositivas 266-267.)

# ADVERTENCIA: solo contra sistemas propios o con autorizacion expresa (Ley 1273/2009).
def ejecutar_con_rotacion(urls_objetivo: list[str], rotaciones: int = 3) -> None:  # recibe las URL y cada cuantas peticiones rotar
    for i, url in enumerate(urls_objetivo):  # recorremos la lista obteniendo el indice i y la url
        if i % rotaciones == 0 and i != 0:  # cada N peticiones, pero no en la primera (i = 0)
            print(f"\n[*] Rotando identidad tras {rotaciones} peticiones...")  # avisamos que vamos a rotar
            rotar_identidad_tor()  # pedimos a TOR un circuito nuevo
            print(f"[+] Nueva IP de salida: {obtener_ip_actual()}")  # mostramos la IP de salida resultante
        try:  # intentamos la peticion y capturamos errores de red
            respuesta = requests.get(url, proxies=TOR_PROXY, timeout=30)  # hacemos el GET a traves de TOR
            print(f"[+] {url} -> HTTP {respuesta.status_code}")  # mostramos la URL y el codigo de estado
        except requests.exceptions.RequestException as e:  # cualquier error de la peticion
            print(f"[-] Error al acceder a {url}: {e}")  # lo reportamos y seguimos con la siguiente URL
