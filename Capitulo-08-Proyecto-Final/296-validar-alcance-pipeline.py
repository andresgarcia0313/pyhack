# Diapositiva 296: Validacion de alcance en Python, parte 2
# Muestra la version pensada para un pipeline: si falta un campo, el script
# sale con codigo de error para que un orquestador sepa que fallo.

# sys permite terminar el programa con un codigo de salida y escribir en el error estandar.
import sys

# Lista corta de campos obligatorios para este ejemplo.
CAMPOS = ["nombre_cliente", "autorizacion_firmada"]


# Funcion que valida y, si algo falta, detiene todo el proceso.
def validar_o_salir(proyecto: dict) -> None:
    # Armamos la lista de campos que faltan o estan vacios.
    faltantes = [c for c in CAMPOS if not proyecto.get(c)]
    # Si hay faltantes, avisamos y salimos.
    if faltantes:
        # file=sys.stderr envia el mensaje al canal de errores, no al de salida normal.
        print("[ERROR] Campos faltantes: " + ", ".join(faltantes), file=sys.stderr)
        # sys.exit(1) termina el programa con codigo 1, que significa "fallo".
        sys.exit(1)                     # el orquestador ve el fallo
    # Si no faltaba nada, el proyecto puede iniciar.
    print("[OK] Validacion completada. El proyecto puede iniciar.")


# Probamos la funcion con un proyecto que si tiene los dos campos llenos.
validar_o_salir({"nombre_cliente": "Lab", "autorizacion_firmada": True})
