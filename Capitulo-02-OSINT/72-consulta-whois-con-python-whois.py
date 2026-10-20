# Diapositiva 72: Uso de python-whois
# Consulta el registro WHOIS de un dominio y muestra sus datos, validando que
# el campo de servidores de nombre puede venir como lista o como una sola cadena.

import whois  # biblioteca que consulta servidores WHOIS y entrega campos ya parseados

dominio = whois.whois("example.com")  # consultamos el registro del dominio de ejemplo
print(f"Registrador:       {dominio.registrar}")  # mostramos quien registro el dominio
print(f"Fecha de creacion: {dominio.creation_date}")  # mostramos cuando se creo el dominio
print(f"Fecha expiracion:  {dominio.expiration_date}")  # mostramos cuando expira el dominio

# Algunos campos son lista cuando hay varios valores: validamos el tipo antes de usarlo.
ns = dominio.name_servers  # tomamos el campo de servidores de nombre
if isinstance(ns, list):  # si el campo es una lista (varios servidores)
    for servidor in ns:  # recorremos cada servidor de la lista
        print(f"  NS: {servidor}")  # mostramos cada servidor de nombre
elif ns:  # si no es lista pero tiene algun valor (una sola cadena)
    print(f"  NS: {ns}")  # mostramos ese unico valor
else:  # si el campo vino vacio o None (comun por privacidad)
    print("  NS: no disponible")  # avisamos que no hay dato
