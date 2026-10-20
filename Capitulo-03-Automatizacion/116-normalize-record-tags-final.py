# Diapositiva 116: Funcion normalize_record, puerto, texto y tags (parte 2)
# Muestra el cierre del manejo de tags (texto, lista u otra cosa) y el
# retorno que SIEMPRE entrega todos los campos del esquema canonico.

# Suponemos un record en construccion y las tags crudas ya tomadas.
record = {}
tags_raw = ["web", "ssl", "activo"]

# Si las tags ya venian como lista, las limpiamos elemento a elemento.
if isinstance(tags_raw, list):
    # Convertimos a texto, quitamos espacios y descartamos los vacios o falsos.
    record["tags"] = [str(t).strip() for t in tags_raw if t]
# Cualquier otro tipo (numero, None, etc.) se vuelve lista vacia para no romper.
else:
    record["tags"] = []


# Demostracion con la funcion completa (resumida aqui para el ejemplo de uso).
def normalize_record(raw: dict, source: str) -> dict:
    # En el ejemplo real aplica todas las normalizaciones de las diapositivas 113 a 116.
    return {"timestamp": "...", "source": source, "target": None,
            "ip_address": "1.1.1.1", "port": 53, "service": None,
            "banner": None, "country": None, "tags": ["dns", "publico"]}


# Ejemplo de uso con un registro crudo.
crudo = {"ip": "1.1.1.1", "port": "53", "tags": "dns, publico"}
# La funcion siempre devuelve el diccionario con todos los campos del esquema.
print(normalize_record(crudo, "cloudflare"))
# {'timestamp': '...', 'source': 'cloudflare', 'target': None,
#  'ip_address': '1.1.1.1', 'port': 53, 'service': None, 'banner': None,
#  'country': None, 'tags': ['dns', 'publico']}
