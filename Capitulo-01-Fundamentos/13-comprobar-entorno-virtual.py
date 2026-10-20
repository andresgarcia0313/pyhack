# Diapositiva 13: Verificacion del interprete y entorno virtual
# Comprueba desde Python mismo si estamos dentro de un entorno virtual,
# comparando dos rutas internas del interprete.

# "import sys" trae el modulo sys, que da informacion del interprete de Python.
import sys

# En un venv, sys.prefix (el entorno) es distinto de sys.base_prefix (el Python base); "!=" significa "distinto de".
dentro = sys.prefix != sys.base_prefix
# sys.version es la version; .split()[0] parte el texto por espacios y toma el primer trozo (el numero). sys.executable es la ruta del Python en uso.
print(f"Python {sys.version.split()[0]} | ejecutable: {sys.executable}")
# Expresion condicional: muestra un texto u otro segun el valor de "dentro" (True o False).
print("Entorno virtual activo" if dentro else "ATENCION: estas usando el Python del sistema")
