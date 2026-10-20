# Diapositiva 300: Dataclass TareaHacking y visualizacion del plan
# Muestra como representar cada tarea del proyecto con un dataclass y como
# imprimir el plan completo en forma de tabla ordenada en la terminal.

# dataclass genera por nosotros el constructor y otros metodos de una clase de datos.
from dataclasses import dataclass
# Literal limita un campo a un conjunto fijo de valores permitidos.
from typing import Literal

# Definimos los unicos estados validos de una tarea.
EstadoTarea = Literal["pendiente", "en_progreso", "completada", "bloqueada"]


# El decorador @dataclass convierte la clase en un contenedor de datos.
@dataclass
class TareaHacking:
    id: str                 # identificador corto de la tarea, por ejemplo T-01
    fase_ptes: str          # fase de PTES a la que pertenece la tarea
    descripcion: str        # que hace la tarea
    herramienta: str        # script que la ejecuta
    activos: list[str]      # lista de objetivos sobre los que trabaja
    criterio_exito: str     # como sabemos que la tarea quedo lista
    estado: EstadoTarea = "pendiente"   # estado inicial; va al final por tener valor por defecto


# Lista de tareas de ejemplo, una por fase del proyecto.
plan = [
    TareaHacking("T-01", "Intelligence Gathering", "DNS y crt.sh",
                 "osint_recon.py", ["scanme.nmap.org"],
                 "Lista de IP y subdominios", "completada"),
    TareaHacking("T-02", "Vulnerability Analysis", "Banners de servicios",
                 "banner_grabber.py", ["192.168.56.101"],
                 "Version de cada puerto abierto", "en_progreso"),
    TareaHacking("T-03", "Exploitation", "Modulo vsftpd en Metasploit",
                 "msf_controller.py", ["192.168.56.101"],
                 "Sesion abierta y documentada", "bloqueada"),
    TareaHacking("T-04", "Reporting", "Informe final",
                 "report_helper.py", [], "Informe entregado"),
]

# Diccionario que traduce cada estado a un marcador de texto que se ve igual en cualquier terminal.
ICONOS = {"pendiente": "[ ]", "en_progreso": "[~]",
          "completada": "[x]", "bloqueada": "[!]"}


# Funcion que imprime la tabla con todas las tareas.
def mostrar_plan(tareas: list[TareaHacking]) -> None:
    # Encabezado de la tabla; :<6 y :<24 reservan ancho y alinean a la izquierda.
    print(f"{'ID':<6} {'FASE':<24} {'ESTADO':<16} DESCRIPCION")
    # Linea separadora de 72 guiones.
    print("-" * 72)
    # Recorremos cada tarea y la imprimimos en columnas.
    for t in tareas:
        print(f"{t.id:<6} {t.fase_ptes:<24} "
              f"{ICONOS[t.estado]} {t.estado:<12} {t.descripcion}")


# Ejecutamos la funcion solo si corremos este archivo directamente.
if __name__ == "__main__":
    mostrar_plan(plan)
