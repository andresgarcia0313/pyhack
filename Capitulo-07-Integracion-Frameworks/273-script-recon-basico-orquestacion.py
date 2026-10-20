# Diapositiva 273: Script de reconocimiento con rutinas reutilizables
# Muestra un script de alto nivel que resuelve un host, escanea unos puertos
# y guarda los resultados en JSON, apoyandose en funciones importadas de un modulo.

import json  # modulo para escribir datos en formato JSON
from utils.network import resolver_host, escanear_puerto  # traemos las funciones de red desde nuestro modulo

OBJETIVO = "scanme.nmap.org"   # host de pruebas autorizado por Nmap
PUERTOS = [22, 80, 443, 8080]  # lista de puertos que vamos a revisar

def main() -> None:  # funcion principal que orquesta el reconocimiento
    ip = resolver_host(OBJETIVO)  # convertimos el nombre del host en su direccion IP
    if ip is None:  # si no se pudo resolver (devolvio None)
        print(f"[!] No se pudo resolver {OBJETIVO}. Abortando.")  # avisamos y
        return  # salimos: sin IP no hay nada que escanear
    resultados = {p: ("abierto" if escanear_puerto(ip, p) else "cerrado")  # para cada puerto guardamos su estado
                  for p in PUERTOS}  # recorremos la lista de puertos con una comprension de diccionario
    with open("resultados_recon.json", "w") as f:  # abrimos el archivo de salida en modo escritura
        json.dump({"objetivo": OBJETIVO, "ip": ip, "puertos": resultados},  # armamos el diccionario con todo
                  f, indent=2)  # lo escribimos en el archivo con sangria de 2 espacios

if __name__ == "__main__":  # si ejecutamos este archivo directamente
    main()  # llamamos a la funcion principal
