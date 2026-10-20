# Diapositiva 180: Codigos de estado HTTP en seguridad
# Muestra como interpretar el codigo de estado al probar rutas:
# un 403 confirma que el recurso existe pero esta protegido.

import requests  # libreria para enviar peticiones HTTP

# Lista de rutas que queremos probar una por una.
rutas = ["/admin", "/noexiste", "/config"]

# Recorremos cada ruta de la lista.
for ruta in rutas:
    # Pedimos la ruta sin seguir redirecciones, para ver el codigo real.
    r = requests.get(f"http://127.0.0.1{ruta}", allow_redirects=False)
    if r.status_code == 403:       # 403 = prohibido: existe pero no tenemos permiso
        print(f"{ruta}: 403 -> EXISTE pero protegido (hallazgo)")
    elif r.status_code == 404:     # 404 = no encontrado: ahi no hay nada
        print(f"{ruta}: 404 -> no existe")
    else:                          # cualquier otro codigo lo mostramos tal cual
        print(f"{ruta}: {r.status_code}")
