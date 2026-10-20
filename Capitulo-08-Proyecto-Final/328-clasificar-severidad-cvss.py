# Diapositiva 328: Clasificacion de severidad con CVSS 3.1
# Muestra una funcion que traduce un puntaje CVSS (de 0 a 10) a su etiqueta
# de severidad: Critica, Alta, Media, Baja o Informativa.

# Funcion que recibe el puntaje y devuelve la etiqueta de texto.
def clasificar_severidad(cvss: float) -> str:
    """Etiqueta de severidad segun los rangos de CVSS 3.1."""
    # Se evalua de mayor a menor: la primera condicion verdadera decide y retorna.
    if cvss >= 9.0:
        return "Critica"
    if cvss >= 7.0:
        return "Alta"
    if cvss >= 4.0:
        return "Media"
    if cvss > 0.0:
        return "Baja"
    # Si el puntaje es 0.0, el hallazgo es solo informativo.
    return "Informativa"


# Probamos la funcion con varios puntajes de ejemplo.
for p in (9.8, 7.5, 5.0, 2.1, 0.0):
    # Mostramos el puntaje y la etiqueta que le corresponde.
    print(f"CVSS {p} -> {clasificar_severidad(p)}")
