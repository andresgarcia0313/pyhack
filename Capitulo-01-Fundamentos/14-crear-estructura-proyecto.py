# Diapositiva 14: Estructura minima de un proyecto
# Crea desde Python el esqueleto de carpetas y archivos de una herramienta
# del curso, util como plantilla repetible.

# "from ... import ..." trae solo la clase Path, que sirve para manejar rutas y archivos.
from pathlib import Path


# Funcion que recibe el nombre del proyecto (texto) y no devuelve nada util (-> None).
def crear_estructura(nombre: str) -> None:
    """Crea el esqueleto minimo de una herramienta del curso."""
    # Path(nombre) crea un objeto ruta con la carpeta base del proyecto.
    base = Path(nombre)
    # "/" une rutas; .mkdir crea la carpeta; parents=True crea las intermedias y exist_ok=True no falla si ya existe.
    (base / "utils").mkdir(parents=True, exist_ok=True)
    # .touch() crea un archivo vacio; __init__.py marca la carpeta como paquete de Python.
    (base / "utils" / "__init__.py").touch()
    # .write_text(...) escribe ese texto dentro del archivo main.py; \n es un salto de linea.
    (base / "main.py").write_text('if __name__ == "__main__":\n    print("ok")\n')
    # Crea un requirements.txt vacio para listar luego las dependencias.
    (base / "requirements.txt").touch()
    # Crea el .gitignore con las rutas que Git no debe subir al repositorio.
    (base / ".gitignore").write_text(".venv/\n__pycache__/\nresultados/\n*.key\n")
    # rglob("*") lista todo lo creado; sorted(...) lo ordena y str(p) lo vuelve texto.
    print(sorted(str(p) for p in base.rglob("*")))


# Llama a la funcion para crear el proyecto llamado "mi_herramienta".
crear_estructura("mi_herramienta")
