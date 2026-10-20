# Diapositiva 160: Parser de banner SSH con expresiones regulares (version completa, diapositivas 159 y 160)
# Muestra como descomponer un banner SSH en protocolo, software, version y distribucion
# usando una expresion regular (patron de busqueda de texto con estructura).

import re  # modulo de expresiones regulares


def parsear_banner_ssh(banner: str) -> dict:  # recibe el banner y devuelve un diccionario con sus partes
    resultado = {"protocolo": None, "software": None,  # empezamos con todo en None (defensivo)
                 "version": None, "distribucion": None}  # si el banner no coincide, devolvemos esto sin fallar
    patron = r"SSH-([\d.]+)-([\w]+)[_/]([\w.]+)\s*(.*)"  # patron: 4 grupos -> protocolo, software, version, resto
    coincidencia = re.match(patron, banner.strip())  # re.match busca el patron al inicio del texto
    if coincidencia:  # si el banner coincidio con el patron
        resultado["protocolo"]    = coincidencia.group(1)  # grupo 1: 2.0
        resultado["software"]     = coincidencia.group(2)  # grupo 2: OpenSSH
        resultado["version"]      = coincidencia.group(3)  # grupo 3: 8.2p1
        resultado["distribucion"] = coincidencia.group(4)  # grupo 4: Ubuntu-4ubuntu0.5
    return resultado  # devuelve el diccionario (lleno o con None si no coincidio)


print(parsear_banner_ssh("SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"))  # prueba con un banner SSH valido
# {'protocolo': '2.0', 'software': 'OpenSSH', 'version': '8.2p1',
#  'distribucion': 'Ubuntu-4ubuntu0.5'}
print(parsear_banner_ssh("220 ProFTPD 1.3.5"))  # prueba con un banner FTP (no coincide con el patron SSH)
# {'protocolo': None, 'software': None, 'version': None, 'distribucion': None}
