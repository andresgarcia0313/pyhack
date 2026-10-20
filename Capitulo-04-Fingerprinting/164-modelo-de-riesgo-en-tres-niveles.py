# Diapositiva 164: Modelo de riesgo preliminar (3 niveles)
# Muestra como asignar riesgo ALTO, MEDIO o BAJO combinando dos factores:
# la exposicion del servicio (publico o interno) y la severidad o antiguedad de la version.

def nivel_riesgo(expuesto_internet: bool, cvss: float, anos_version: int) -> str:  # recibe los tres datos
    """Combina exposicion, severidad CVSS y antiguedad."""  # texto de ayuda
    if expuesto_internet and cvss >= 7.0:  # publico y vulnerabilidad grave (CVSS 7.0 o mas)
        return "ALTO"  # el peor escenario
    if (not expuesto_internet and cvss >= 7.0) or anos_version >= 2:  # interno con fallo grave, o version vieja
        return "MEDIO"  # riesgo intermedio
    return "BAJO"  # el resto: riesgo bajo


print(nivel_riesgo(expuesto_internet=True,  cvss=9.8, anos_version=5))  # ALTO
print(nivel_riesgo(expuesto_internet=False, cvss=9.8, anos_version=1))  # MEDIO
print(nivel_riesgo(expuesto_internet=False, cvss=3.0, anos_version=0))  # BAJO
