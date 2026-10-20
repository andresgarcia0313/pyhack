# -*- coding: utf-8 -*-
# Diapositiva 242: Tipos de reenvio de puertos SSH para pivoting
# Resume los tres tipos de reenvio de puertos y la direccion del tunel en cada uno.

# Diccionario con los tres tipos de reenvio de puertos SSH y su direccion.
TUNELES = {
    "-L (local)":    "cliente -> servidor -> destino  (alcanzar servicio interno)",
    "-R (remoto)":   "servidor -> cliente -> destino  (exponer servicio propio)",
    "-D (dinamico)": "cliente como proxy SOCKS         (enrutar todo el trafico)",
}

# Recorre el diccionario mostrando cada tipo con su descripcion.
for tipo, descripcion in TUNELES.items():  # .items() da pares (clave, valor)
    print(tipo, "->", descripcion)  # imprime el tipo de tunel y que hace

# Base de datos interna visible solo desde el host puente -> usar -L (local).
