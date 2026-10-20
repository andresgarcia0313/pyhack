# Diapositiva 306: Filtro de riesgos criticos activos
# Muestra como representar los riesgos del proyecto con un dataclass y filtrar
# solo los que siguen activos y tienen impacto alto o critico.

# dataclass genera el constructor y otros metodos de la clase de datos.
from dataclasses import dataclass
# Literal limita un campo a un conjunto fijo de valores.
from typing import Literal

# Los cuatro niveles validos de probabilidad e impacto.
NivelRiesgo = Literal["bajo", "medio", "alto", "critico"]


# Clase de datos que describe un riesgo del proyecto.
@dataclass
class Riesgo:
    id: str                 # identificador del riesgo, por ejemplo R-01
    descripcion: str        # en que consiste el riesgo
    probabilidad: NivelRiesgo   # que tan probable es
    impacto: NivelRiesgo    # que tan grave seria
    mitigacion: str         # como se reduce
    responsable: str        # persona a cargo
    activo: bool = True      # True mientras el riesgo siga abierto


# Lista de riesgos de ejemplo; R-03 esta marcado como inactivo porque ya se mitigo.
matriz = [
    Riesgo("R-01", "Caida de servicio por escaneo agresivo", "medio", "alto",
           "Limitar tasa; ventana acordada", "Pentester lider"),
    Riesgo("R-02", "Exposicion accidental de datos sensibles", "bajo", "critico",
           "Cifrar hallazgos; NDA firmado", "Ana Gomez"),
    Riesgo("R-03", "Expansion no autorizada del alcance", "alto", "alto",
           "Confirmar por escrito con el cliente", "Project Manager", activo=False),
    Riesgo("R-04", "Alertas del cliente detienen la prueba", "medio", "medio",
           "Coordinar con el equipo de defensa", "Pentester tecnico"),
]


# Funcion que deja solo los riesgos activos con impacto critico o alto.
def riesgos_activos_criticos(riesgos: list[Riesgo]) -> list[Riesgo]:
    """Filtra riesgos activos con impacto critico o alto."""
    # r.activo debe ser True y el impacto debe estar en la tupla de valores graves.
    return [r for r in riesgos if r.activo and r.impacto in ("critico", "alto")]


# Obtenemos la lista de riesgos criticos activos.
criticos = riesgos_activos_criticos(matriz)
# Si la lista tiene elementos, mostramos una alerta por cada uno.
if criticos:
    print(f"[ALERTA] {len(criticos)} riesgo(s) de alto impacto activos:")
    for r in criticos:
        print(f"  [{r.id}] {r.descripcion} - {r.responsable}")
# Si no hay ninguno, mensaje de tranquilidad.
else:
    print("[OK] No hay riesgos activos de alto impacto.")
