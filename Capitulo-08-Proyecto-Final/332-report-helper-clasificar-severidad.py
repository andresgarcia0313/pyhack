# Diapositiva 332: Script report_helper.py, crear hallazgo y clasificar severidad, parte 2
# Muestra la funcion clasificar_severidad, que convierte el puntaje CVSS en
# una etiqueta, evaluando de mayor a menor para que gane el umbral mas alto.

# Funcion que traduce el puntaje CVSS a su etiqueta de severidad.
def clasificar_severidad(cvss: float) -> str:
    # Si el puntaje es 9.0 o mas, es Critica.
    if cvss >= 9.0:
        return "Critica"
    # Entre 7.0 y 8.9, es Alta.
    if cvss >= 7.0:
        return "Alta"
    # Entre 4.0 y 6.9, es Media.
    if cvss >= 4.0:
        return "Media"
    # Entre 0.1 y 3.9, es Baja.
    if cvss > 0.0:
        return "Baja"
    # Si es 0.0, solo es Informativa.
    return "Informativa"


# El diccionario de crear_hallazgo termina con estos dos campos:
#   "estado": "Abierto",
#   "evidencias": [],
# Probamos la funcion con el puntaje mas alto y con el mas bajo.
print(clasificar_severidad(9.8), clasificar_severidad(0.0))
