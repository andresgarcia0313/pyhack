# Diapositiva 158: Descomposicion semantica de un banner
# Muestra como una respuesta HTTP revela varias capas a la vez: servidor web,
# lenguaje del backend y gestor de contenidos (CMS), leyendo linea por linea.

# Cabecera HTTP con cuatro capas de informacion a la vez
respuesta_http = """HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
X-Powered-By: PHP/7.4.3
X-Generator: Drupal 9 (https://www.drupal.org)"""  # texto de ejemplo de una respuesta HTTP (varias lineas)

for linea in respuesta_http.splitlines():  # recorre la respuesta linea por linea
    if linea.startswith("Server:"):      print("Servidor web :", linea.split(": ",1)[1])  # separa por ": " y toma el valor
    elif linea.startswith("X-Powered"):  print("Lenguaje     :", linea.split(": ",1)[1])  # lenguaje del backend
    elif linea.startswith("X-Generator"):print("CMS          :", linea.split(": ",1)[1])  # gestor de contenidos
# Servidor web : nginx/1.18.0 (Ubuntu)
# Lenguaje     : PHP/7.4.3
# CMS          : Drupal 9 (https://www.drupal.org)
