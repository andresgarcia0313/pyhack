# Diapositiva 161: Flujo de parsing de un banner SSH
# Muestra la cadena completa: de banner crudo a datos estructurados y a una decision de riesgo.
# Se incluye el parser de la diapositiva 160 para que el ejemplo sea ejecutable por si solo.

import re  # expresiones regulares


def parsear_banner_ssh(banner: str) -> dict:  # mismo parser de la diapositiva 160 (necesario aqui)
    resultado = {"protocolo": None, "software": None,
                 "version": None, "distribucion": None}  # valores por defecto en None
    patron = r"SSH-([\d.]+)-([\w]+)[_/]([\w.]+)\s*(.*)"  # patron de 4 grupos
    coincidencia = re.match(patron, banner.strip())  # intenta encajar el patron al inicio
    if coincidencia:  # si coincidio
        resultado["protocolo"]    = coincidencia.group(1)  # protocolo
        resultado["software"]     = coincidencia.group(2)  # software
        resultado["version"]      = coincidencia.group(3)  # version
        resultado["distribucion"] = coincidencia.group(4)  # distribucion
    return resultado  # devuelve el diccionario


# Cadena completa: crudo -> estructurado -> decision de riesgo (conceptual)
banner = "SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.10"  # banner crudo de ejemplo
datos = parsear_banner_ssh(banner)           # paso 1: estructurar el banner en un diccionario
version = datos["version"]                    # '7.2p2' -> paso 2: tomar el campo clave (la version)
# paso 3: decidir (aqui simplificado; en real se consulta NVD)
riesgo = "ALTO" if version and version.startswith("7.2") else "por revisar"  # regla simple de ejemplo
print(f"{datos['software']} {version} -> SO {datos['distribucion']} -> riesgo {riesgo}")  # muestra el resultado
# OpenSSH 7.2p2 -> SO Ubuntu-4ubuntu2.10 -> riesgo ALTO
