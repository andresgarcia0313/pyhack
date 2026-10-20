# Diapositiva 83: Paginacion por cursor y cabecera Link
# Muestra la paginacion por cabecera Link (estilo GitHub): el servidor manda
# la URL de la pagina siguiente y "requests" la deja lista en r.links.

# Traemos la libreria "requests" para pedir datos a servicios web (APIs).
import requests

# Guardamos la direccion de la primera pagina que vamos a consultar.
url = "https://api.github.com/repositories"
# "while url" repite mientras "url" tenga un valor; si queda vacio o None, para.
while url:
    # Pedimos los datos; en "headers" indicamos el formato que esperamos recibir.
    r = requests.get(url, headers={"Accept": "application/vnd.github+json"}, timeout=10)
    # Si la respuesta trae un error HTTP, lanza una excepcion y no seguimos.
    r.raise_for_status()
    # Recorremos cada repositorio de la lista que vino en la respuesta.
    for repo in r.json():
        pass  # procesar(repo)
    # requests expone la cabecera Link ya parseada:
    # Tomamos la URL de la pagina "next"; si no hay, el resultado es None y el while para.
    url = r.links.get("next", {}).get("url")   # None cuando no hay siguiente
