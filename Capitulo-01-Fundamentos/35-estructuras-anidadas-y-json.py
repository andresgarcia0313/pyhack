# Diapositiva 35: Estructuras anidadas, jerarquia host, puerto y banner
# Muestra una estructura anidada (host -> puertos -> datos) y la trampa de las
# claves numericas al pasar por JSON (vuelven como texto).

# json convierte entre estructuras de Python y texto JSON.
import json

# Diccionario anidado: host, dentro "puertos", dentro el puerto 22 con su estado y banner.
resultados = {"192.168.56.101": {"puertos": {22: {"estado": "abierto", "banner": "OpenSSH_8.2"}}}}
# dumps convierte la estructura a texto JSON.
texto = json.dumps(resultados)
# loads convierte el texto JSON de vuelta a estructura de Python.
recuperado = json.loads(texto)

# Muestra el texto JSON; la clave 22 aparece como "22".
print(texto)
# Las claves de puertos ahora son texto (str), no enteros.
print(list(recuperado["192.168.56.101"]["puertos"].keys()))    # ahora son str
# Acceso seguro encadenando .get() en cada nivel para no fallar si algo falta.
banner = recuperado.get("192.168.56.101", {}).get("puertos", {}).get("22", {}).get("banner")
# Muestra el banner recuperado.
print(f"[+] Banner: {banner}")
